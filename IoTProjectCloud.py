#import custom_temp
#import PushButton
import custom_temp as ct
import google_weather as gw
import RPi.GPIO as GPIO
import time
import ReadCloudState as rcs
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT)#ch3
GPIO.setup(5, GPIO.OUT)#ch1
GPIO.setup(26, GPIO.OUT)#ch2
GPIO.setup(1, GPIO.OUT)#ch4


while True:
    state = rcs.readDataState()
    state = 28
    weather = gw.weather()
    waterTemperature=ct.read_temp()
    print("User input temperature",state)
    print (weather)
    print (waterTemperature)
    if waterTemperature is not None and weather is not None and state is not None:
        if waterTemperature>state:
            print("Temperature will get hotter by \t", state, "degree")
            
            while True:
                #state = rcs.readDataState()
                print("Temperature will get hotter by \t", state, "degree")
                if state<=waterTemperature:
                    break
                #starts heating
                GPIO.output(5, False)
                GPIO.output(13, False)
                GPIO.output(26, False)
                GPIO.output(1, True)

        elif waterTemperature<state:
            print ("Temperature will be cooled by \t", state, "degree")
            while True:
                if state>waterTemperature:
                    break
                #starts Cooling
                GPIO.output(5, True)#ch5 -off
                GPIO.output(13, True)#ch13 -off
                GPIO.output(26, True)#ch26 -off
                GPIO.output(1, False)#ch1 -on
                    
        elif state == "default":
            print ("default temperature is set")
            while True:
                if waterTemperature <= weather:
                    #Match with surrounding weather
                    GPIO.output(5, True)
                    GPIO.output(13, True)
                    GPIO.output(26, True)
                    GPIO.output(1, False)
                else:
                    GPIO.output(5, False)
                    GPIO.output(13, False)
                    GPIO.output(26, False)
                    GPIO.output(1, True)
        else:
            GPIO.output(5, True)
            GPIO.output(13, True)
            GPIO.output(26, True)
            GPIO.output(1, True)

