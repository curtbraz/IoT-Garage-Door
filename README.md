# IoT-Garage-Door
Retrofit Any Existing Garage Door Motor Into a Google Voice / Alexa Internet Enabled Smart Door Opener

I thought it would be fun to get into the Home Automation space and create an Internet Connected Smart Garage Door Opener for my very old garage door.  I only own one remote, and the range is awful.  I wanted to be able to leverage my Google Home Mini or my Android via Google Assistant to open and close the door anywhere in the world.  Since I don't have the money to buy a new smart garage door motor, I went about creating one myself with an extra Raspberry Pi and a 5v Relay I had laying around.  Here are the steps to recreate!  In a future phase, I'll have a counter implemented to report if the door is currently open or closed for remote use.

Instructions : 


1) Set up a Raspberry Pi with Raspbian (I used a model B, if you use an A you'll want to supply a USB wifi adapter)

2) Make sure Python, PHP, and Apache are Installed

3) Deploy API.php and GarageDoor.py to /var/www/html/ and Make Sure They are Executable (chmod +x)

4) Generate a Unique GUID/Token (cat /proc/sys/kernel/random/uuid) and Add to "Token" Variable in index.php

5) Set up Relay and GPIO as Pictured in Screenshot Below (I used Pin 17, So if You Choose Something Else Update the "Pin" Variable in GarageDoor.py)

6) Port Forward Your Router to Make Your Pi on TCP 80 Accessible to the Internet

7) Create an IFTTT.com Applet for Google Assistant With an Outgoing Webhook (GET Request) as Pictured Below, Using your URL (http://YOUR-PUBLIC-IP/API.php?Token=YOUR-GUID-HERE)

8) Say "Ok Google, Open the Garage Door" From Anywhere in the Wold :)

Images : 


![Finished Product](https://i.imgur.com/QHwhLrr.jpg)

![GPIO and Relay Layout](https://i.imgur.com/HqlKxyw.jpg)

![IFTTT Applet Recipie](https://i.imgur.com/wWyx5RH.png)

![Using My Voice to Open!](https://i.imgur.com/KPEASWy.png)
