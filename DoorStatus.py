#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import datetime
import pymysql.cursors

count = 0

CurrentTime = time.time()
CurrentTime = datetime.datetime.fromtimestamp(CurrentTime).strftime('%Y-%m-%d %H:%M:%S')

# Runs for Just Under a Minute
t_end = time.time() + 55
while time.time() < t_end:

        # Sets up GPIO Pin 23 for Input
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(23, GPIO.IN)

        # Reads The Current State of the Pin (1 for on, 0 for Off)
        i = GPIO.input(23)
        
        # If the Value is 1 at all During the Minute, It Can be Assumed "Open"
        # Magnetic Reed Sensor is not Consistent, Need to do it This Way
        count = i + count

        # Add the Value and Sleep 5 Seconds      
        time.sleep(5)

        # Resets the GPIO Pin
        GPIO.cleanup()

# If, During the Minute, a Value of 1 Was Detected, The Door was Open.  Otherwise, it's Closed
if count > 0:
        Status = "Open"
elif count < 1:
        Status = "Closed"



# Connect to the database (Alter Variables to Match Your Setup)
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='GarageDoor',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

# Insert Open/Closed State Into MySQL Database Along With Timestamp
try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `DoorStatus` (`Status`, `TS`) VALUES (%s, %s)"
        cursor.execute(sql, (Status, CurrentTime))

    # Commits Changes to DB
    connection.commit()
finally:
    connection.close()
