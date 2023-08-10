import urllib.request
import json
import time

channel_ID = "1887179"

mqtt_host = "mqtt3.thingspeak.com"

# Your MQTT credentials for the device
mqtt_client_ID = "EzU1CCcjLwknNjI6FxMUKBc"
mqtt_username  = "EzU1CCcjLwknNjI6FxMUKBc"
mqtt_password  = "WZtoNS8DUEC+n5rfB9Cdl1W3"

t_transport = "websockets"
t_port = 80

topic = "channels/" + "1887179" + "/subscribe"


READ_API_KEY='UVNOTX3T6I5DPIOM'
CHANNEL_ID= '1887179'
global TS
def readDataState():
#while True:
    TS = urllib.request.urlopen("http://api.thingspeak.com/channels/%s/feeds/last.json?api_key=%s" %(CHANNEL_ID,READ_API_KEY))
    payload = "field3"
    response = TS.read()
    data=json.loads(response)

    a = data['field3']

    #print (a )
    TS.close()
    #return a

#print(readDataState())
