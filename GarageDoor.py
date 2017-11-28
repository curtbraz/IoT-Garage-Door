#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# Set GPIO Pin Here (I Used 17)
pin = 17

# Set up GPIO
GPIO.setup(pin, GPIO.OUT)
GPIO.output(pin, GPIO.HIGH)

# Time in Seconds for Door to Open / Close
DoorTimeToClose = 12

# Initiate Door Toggle
GPIO.output(pin, GPIO.LOW)
print "Toggling Garage Door.."
time.sleep(DoorTimeToClose);

# Reset
GPIO.cleanup()
