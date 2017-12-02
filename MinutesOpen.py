#!/usr/bin/python
import pymysql.cursors
import requests

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='GarageDoor',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Read a single record
        sql = "select TIMESTAMPDIFF(MINUTE,MAX(TS),iq.LastOpen) AS `MinutesOpen` from `DoorStatus` INNER JOIN (SELECT MAX(TS) as `LastOpen` FROM `DoorStatus` WHERE `Status` = 'Open') iq WHERE `Status` = 'Closed';"
        cursor.execute(sql)
        result = cursor.fetchone()
        Minutes = int(result['MinutesOpen'])
finally:
    connection.close()

print Minutes

if Minutes > 9:
        r = requests.get('https://maker.ifttt.com/trigger/Garage_Left_Open/with/key/YOUR_IFTTT_INCOMING_WEBOOK)
        r.json()
