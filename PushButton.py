import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Button to GPIO24
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Button to GPIO23
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Button to GPIO25
#GPIO.setup(24, GPIO.OUT)  #LED to GPIO24

Temperature = 25

def customize_button():
    global Temperature
    try:
    #while True:
        temp_increase = GPIO.input(23)
        temp_decrease = GPIO.input(24)
        temp_default = GPIO.input(25)
            #print (button_state)
        if temp_increase == False:
            Temperature+=1
            heat = "heat"
            return heat 
                 
        if temp_decrease == False:
            Temperature-=1

            cool = "cool"
            return cool 
            
        if temp_default == False:
            Temperature=20
            default = "default"
            return default 
    except:
        print("Error in Button (PushButton.py -> customize_button)!!!")
        GPIO.cleanup()

#customize_button()

'''while True:
    button = customize_button()
    if button != None:
        print(button)
        button = None'''