import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def shutdown(channel):
    os.system("sudo shutdown -h now")

GPIO.add_event_detect(21, GPIO.FALLING, callback=shutdown, bouncetime=1000)

while 1:
    time.sleep(1)
