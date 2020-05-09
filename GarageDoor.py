#!/usr/bin/python

## SET YOUR TOKEN HERE (uuidgen on Linux)
token = "50060667-7fad-4d9d-8b06-8d62a8012fad"

import json
import RPi.GPIO as GPIO
import time
from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

#    def do_GET(self):
#        self.send_response(200)
#        self.end_headers()
#        self.wfile.write(b'404 Not Found')

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        response.write(body)
        receivedtoken = response.getvalue()
        resp_dict = json.loads(receivedtoken)
        resptoken = resp_dict['token']
        if token == resptoken:
            GPIO.setmode(GPIO.BCM)

            # Set GPIO Pin Here (I Used 17)
            pin = 17

            # Set up GPIO
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.HIGH)

            # Set Time in Seconds for Door to Open / Close
            DoorTimeToClose = 12

            # Initiate Door Toggle
            GPIO.output(pin, GPIO.LOW)
            print ("Toggling Garage Door..")
            time.sleep(DoorTimeToClose);

            # Reset
            GPIO.cleanup()
        
httpd = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()
