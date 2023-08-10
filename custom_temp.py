#import os
import glob
import urllib.request

import paho.mqtt.publish as publish
import psutil
import string

channel_ID = "1887179"

mqtt_host = "mqtt3.thingspeak.com"

# Your MQTT credentials for the device
mqtt_client_ID = "EzU1CCcjLwknNjI6FxMUKBc"
mqtt_username  = "EzU1CCcjLwknNjI6FxMUKBc"
mqtt_password  = "WZtoNS8DUEC+n5rfB9Cdl1W3"

t_transport = "websockets"
t_port = 80

topic = "channels/" + "1887179" + "/publish"


base_dir = '/sys/bus/w1/devices/'
# Get all the filenames begin with 28 in the path base_dir.
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines
 
def read_temp():
    lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        # Read the temperature .
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        payload = "field2=" + str(temp_c)
        try:
            #print ("Writing Payload = ", payload," to host: ", mqtt_host)
            publish.single(topic, payload, hostname=mqtt_host, transport=t_transport, port=t_port, client_id=mqtt_client_ID, auth={'username':mqtt_username,'password':mqtt_password})

        except Exception as e:
            print (e) 
        print ("Water Temperature is: ", temp_c)
        return temp_c
        #return temp_c

'''while True:
    read_temp()
    temp = read_temp()
    print(temp)
    payload = "field2=" + str(temp)

    try:
        #print ("Writing Payload = ", payload," to host: ", mqtt_host, " clientID= ", mqtt_client_ID, " User ", mqtt_username, " PWD ", mqtt_password)
        publish.single(topic, payload, hostname=mqtt_host, transport=t_transport, port=t_port, client_id=mqtt_client_ID, auth={'username':mqtt_username,'password':mqtt_password})

    except Exception as e:
        print (e) 
'''
    
    

    #if temp>
