# built-in
import ast
import json
import random
import time
import string
import subprocess
from datetime import datetime

# third-party
import paho.mqtt.client as mqtt

# local
from epibox.startup import startup 
from epibox.common.disconnect_system import disconnect_system
from epibox.common.create_folder import create_folder
from epibox.common.open_file import open_file
from epibox.common.write_file import write_annot_file
from epibox.common.start_system import start_system
from epibox.common.run_system import run_system
from epibox.common.connect_device import connect_device
from epibox.common import process_data


def random_str(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

def on_message(client, userdata, message):
    
    message = str(message.payload.decode("utf-8"))
    message = ast.literal_eval(message)
    print("message received: ", message)
    
    if message[0] == 'RESTART':
        client.loop_stop()
        startup.main()
        
    elif message[0] == 'INTERRUPT':
        client.keepAlive = False
    
    elif message[0] == 'PAUSE ACQ':
        print('PAUSING ACQUISITION')
        global pause_acq
        pause_acq = True
        
    elif message[0] == 'RESUME ACQ':
        print('RESUMING ACQUISITION')
        pause_acq = False
        
    elif message[0] == 'ANNOTATION':
        print('RECEIVED ANNOT {} ----------------------'.format(message[1]))
        global new_annot
        global write_annot
        new_annot = message[1]
        write_annot = True
        
    elif message[0] == 'TURN OFF':
        print('TURNING OFF RPI')
        client.publish(topic='rpi', payload=str(['TURNED OFF']))
    
    elif message[0] == 'TURNED OFF':
        subprocess.run(['sudo', 'shutdown', '-h', 'now'])

#****************************** MAIN SCRIPT ***********************************

def main(devices):
    
    try:
        
        client_name = random_str(6)
        print('Client name (acquisition):', client_name)
        host_name = '192.168.0.10'
        topic = 'rpi'
        
        client = mqtt.Client(client_name)
        setattr(client, 'keepAlive', True)
        client.username_pw_set(username='preepiseizures', password='preepiseizures')
        client.connect(host_name)
        client.subscribe(topic)
        client.on_message = on_message
        client.loop_start()
        print('Successfully subcribed to topic', topic)
        init = False
        client.publish('rpi', "['STARTING']")

        with open('/home/pi/Documents/epibox/args.json', 'r') as json_file:
            opt = json_file.read()
            
        opt = ast.literal_eval(opt)
        
        if not opt['channels']:
            channels = []
            for device in opt['devices_mac']:
                for i in range(1,7):
                    channels += [[device,str(i)]]
            sensors = ['-' for i in range(len(channels))]
        
        else:
            channels = []
            sensors = []
            for triplet in opt['channels']:
                channels += [triplet[:2]] 
                sensors += [triplet[2]]
        
        saveRaw = bool(opt['saveRaw'])
        service = opt['service']
        
        global write_annot
        global new_annot
        global pause_acq

        write_annot = False
        pause_acq = False
        already_notified_pause = False
        system_started = False
        
        print('ID: {}'.format(opt['patient_id']))
        print('folder: {}'.format(opt['initial_dir']))
        print('fs: {}'.format(opt['fs']))
        print('saveRaw: {}'.format(saveRaw))
        print('channels: {}'.format(channels))
        print('devices: {}'.format(opt['devices_mac']))
        print('sensors: {}'.format(sensors))
        print('service: {}'.format(service))
        print('Devices in list: {}'.format([d.macAddress for d in devices]))
                            
                            
        # Use/create the patient folder =============================================================== 
        directory = create_folder(opt['initial_dir'], '{}'.format(opt['patient_id']), service)
        already_timed_out = False   
        
        try:
            a_file, annot_file, drift_log_file, save_fmt, header = open_file(directory, devices, channels, sensors, opt['fs'], saveRaw, service)

        except Exception as e:
            print(e)
            client.publish('rpi', "['ERROR']")
            client.loop_stop()
            
            # Disconnect the system
            print('Could not open the files')
            disconnect_system(devices, service, files_open=False)
            system_started = False
            pid = subprocess.run(['sudo', 'pgrep', 'python'], capture_output=True, text=True).stdout.split('\n')[:-1]
            for p in pid:
                subprocess.run(['kill', '-9', p])
             

        # Starting Acquisition LOOP =========================================================================
        try:
            while client.keepAlive == True:
                
                if pause_acq and not already_notified_pause:
                    
                    sync_param['mode'] = 0
                    
                    for i,device in enumerate(devices):
                        try:
                            device.stop()
                        except Exception as e:
                            print(e)
                            continue
                     
                    client.publish('rpi', "['PAUSED']")
                    already_notified_pause = True
                
                elif not pause_acq:
                    
                    if (already_notified_pause):
                        print('paused and restarting')
                        client.publish('rpi', "['RECONNECTING']")
                        
                    already_notified_pause = False
                    
                    if not system_started:
                    
                        try:
                        
                            _, t_disp, sync_param = start_system(devices, a_file, drift_log_file, opt['fs'], channels, sensors, save_fmt, header)
                            system_started = True
                            client.publish('rpi', "['ACQUISITION ON']")
        
                            t_display = process_data.decimate(t_disp, opt['fs'])
                            print('t_display: {}'.format(t_display))
                            json_data = json.dumps(['DATA', t_display, channels, sensors])
                            client.publish('rpi', json_data)
                            already_timed_out = False
                            
                            
                            
                        except Exception as e:
                            print(e)
                            pass
                    
                    # Acquisition LOOP =========================================================================
                    # try to read from the device--------------------------------------------------------------------------------------------------
                    
                    if write_annot:
                        print('SAVED ANNOT')
                        write_annot_file(annot_file, new_annot)
                        write_annot = False
                
                    try:
                        _, t_disp, a_file, drift_log_file, sync_param = run_system(devices, a_file, annot_file, drift_log_file, sync_param, directory, channels, sensors, opt['fs'], save_fmt, header)
                    
                        t_display = process_data.decimate(t_disp, opt['fs'])
                                    
                        json_data = json.dumps(['DATA', t_display, channels, sensors])
                        client.publish('rpi', json_data)
                        already_timed_out = False
                        
                    # Handle misconnection of the devices--------------------------------------------------------------------------------------------
                    except Exception as e:
                        print('')
                        print('')
                        print('The system has stopped running because ' + str(e) + '! Please check Modules!')
                        print('Trying to Reconnect....')
                        client.publish('rpi', "['RECONNECTING']")
                        
                        # Disconnect the system
                        now = datetime.now()
                        save_time = now.strftime("%H-%M-%S").rstrip('0')
                        write_annot_file(annot_file, ['disconnection', save_time])
                        
                        disconnect_system(devices, service, a_file, annot_file, drift_log_file)
                        devices = []
                        system_started = False
                        sync_param['mode'] = 0
                        
                        # Reconnect the devices
                        try:
                            #*********** Connection to ScientISST devices ***********#
                            for i, mac in enumerate(opt['devices_mac']):
                            
                                init_connect_time = time.time()
                                print('Searching for Module...' + mac)
                                
                                while client.keepAlive == True:
    
                                    if (time.time() - init_connect_time) > 120:
                                        client.publish('rpi', "['STOPPED']")
                                        client.loop_stop()
                                        print('TIMEOUT')
                                        
                                        # Disconnect the system
                                        disconnect_system(devices, service, a_file, annot_file, drift_log_file)
                                        client.keepAlive == False
                                        pass
                                    
                                    try:
                                        if already_timed_out == True and time.time() - init_connect_time > 10:
                                            already_timed_out = False
                                        
                                        connected = False
                                        time.sleep(5)
                                        connected, devices = connect_device(mac, client, devices, service)
                                        
                                        if connected and mac in [d.macAddress for d in devices]:
                                            now = datetime.now()
                                            save_time = now.strftime("%H-%M-%S").rstrip('0')
                                            write_annot_file(annot_file, ['reconnection', save_time])
                                            break
    
                                    except Exception as e:
                                        print(e)
                                        print('HERE Failed at connecting to BITalino')
                                        sync_param['mode'] = 0
                                        if already_timed_out == False and time.time() - init_connect_time > 10:
                                            timeout_json = json.dumps(['TIMEOUT', '{}'.format(mac)])
                                            client.publish('rpi', timeout_json)
                                            print('SENT TIMEOUT')
                                            already_timed_out = True
                                            init_connect_time = time.time()
                            
                            print('Devices in list: {}'.format([d.macAddress for d in devices]))
                            
                            a_file, annot_file, drift_log_file, save_fmt, header = open_file(directory, devices, channels, sensors, opt['fs'], saveRaw, service)
                        
                            # Acquisition LOOP =========================================================================
                                                           
                            _, t_disp, sync_param = start_system(devices, a_file, drift_log_file, opt['fs'], channels, sensors, save_fmt, header)
                            system_started = True
                            print('The system is running again ...')
                            client.publish('rpi', "['ACQUISITION ON']")
                            
                            t_display = process_data.decimate(t_disp, opt['fs'])
                                        
                            json_data = json.dumps(['DATA', t_display, channels, sensors])
                            client.publish('rpi', json_data)
                            already_timed_out = False
                            
                        except:
                            pass
            
                else:
                    pass
            
        except KeyboardInterrupt:
            print('')
            print('You have stopped the acquistion. Saving all the files ...')
            client.publish('rpi', "['STOPPED']")
            client.loop_stop()
            
            # Disconnect the system
            disconnect_system(devices, service, a_file, annot_file, drift_log_file)
            client.keepAlive == False
            pass
    
            
            # -----------------------------------------------------------------------------------------------------------------------------------------
        
        print('')
        client.publish('rpi', "['STOPPED']")
        client.loop_stop()
        
        # Disconnect the system
        disconnect_system(devices, a_file, annot_file, drift_log_file)
        system_started = False
        print('You have stopped the acquistion. Saving all the files ...')
        time.sleep(3)
        pid = subprocess.run(['sudo', 'pgrep', 'python'], capture_output=True, text=True).stdout.split('\n')[:-1]
        for p in pid:
            subprocess.run(['kill', '-9', p])
        
    except Exception as e:
        print(e)
        client.publish('rpi', "['STOPPED']")
        client.loop_stop()
        
        # Disconnect the system
        disconnect_system(devices, service, a_file, annot_file, drift_log_file)
        system_started = False
        print('You have stopped the acquistion. Saving all the files ...')
        time.sleep(3)
        pid = subprocess.run(['sudo', 'pgrep', 'python'], capture_output=True, text=True).stdout.split('\n')[:-1]
        for p in pid:
            subprocess.run(['kill', '-9', p])
    
    # =========================================================================================================