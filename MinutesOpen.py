#!/usr/bin/python
import pymysql.cursors
import urllib2

# Connect to the database (Change Variables to Match Your Instance)
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='GarageDoor',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

# Calculates Time in Minutes Since the Last Time the Door Was Closed
try:
    with connection.cursor() as cursor:
        sql = "select TIMESTAMPDIFF(MINUTE,MAX(TS),iq.LastOpen) AS `MinutesOpen` from `DoorStatus` INNER JOIN (SELECT MAX(TS) as `LastOpen` FROM `DoorStatus` WHERE `Status` = 'Open') iq WHERE `Status` = 'Closed';"
        cursor.execute(sql)
        result = cursor.fetchone()
        Minutes = int(result['MinutesOpen'])
finally:
    connection.close()

# If the Door Was Open 10, 20, or 30 Minutes (or longer), Trigger IFTTT SMS Text Message via Webhook Request
if Minutes in (10,20,30,60,180,360,1440):
        urllib2.urlopen('https://maker.ifttt.com/trigger/Garage_Left_Open/with/key/YOUR-IFTTT-INCOMING-WEBHOOK').read()
