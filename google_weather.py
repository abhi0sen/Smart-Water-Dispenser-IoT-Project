import Adafruit_DHT
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


def weather():  
    humidity, temp = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 2)

    print("Surrounding Temperature is: ", temp)
    payload = "field1=" + str(temp)

    try:
        #print ("Writing Payload = ", payload," to host: ", mqtt_host, " clientID= ", mqtt_client_ID, " User ", mqtt_username, " PWD ", mqtt_password)
        publish.single(topic, payload, hostname=mqtt_host, transport=t_transport, port=t_port, client_id=mqtt_client_ID, auth={'username':mqtt_username,'password':mqtt_password})

    except Exception as e:
        print (e) 
    return temp
    #f = urllib.request.urlopen(a.encode('utf-8'))

#f.close()
'''
while True:
    weather()
    '''
