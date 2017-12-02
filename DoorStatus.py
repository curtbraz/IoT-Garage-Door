#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import datetime
import pymysql.cursors

count = 0

CurrentTime = time.time()
CurrentTime = datetime.datetime.fromtimestamp(CurrentTime).strftime('%Y-%m-%d %H:%M:%S')

t_end = time.time() + 55
while time.time() < t_end:

        GPIO.setmode(GPIO.BCM)

        GPIO.setup(23, GPIO.IN)

        i = GPIO.input(23)

        count = i + count

        time.sleep(5)

        GPIO.cleanup()


if count > 0:
        Status = "Open"
elif count < 1:
        Status = "Closed"



# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='GarageDoor',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `DoorStatus` (`Status`, `TS`) VALUES (%s, %s)"
        cursor.execute(sql, (Status, CurrentTime))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()
finally:
    connection.close()
