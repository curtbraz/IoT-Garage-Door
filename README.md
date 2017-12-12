# IoT-Garage-Door
Retrofit Any Existing Garage Door Motor Into a Google Voice / Alexa Internet Enabled Smart Door Opener

I thought it would be fun to get into the Home Automation space and create an Internet Connected Smart Garage Door Opener for my very old garage door.  I only own one remote, and the range is awful.  I wanted to be able to leverage my Google Home Mini or my Android via Google Assistant to open and close the door anywhere in the world.  Since I don't have the money to buy a new smart garage door motor, I went about creating one myself with an extra Raspberry Pi and a 5v Relay I had laying around.  Here are the steps to recreate!  

There is also DoorStatus.py and MinutesOpen.py which can be used in combination with a magnetic reed switch, as I have setup, to notify when the door is left open for X minutes.  

# Instructions : 


1) Set up a Raspberry Pi with Raspbian (I used a model B, if you use an A you'll want to supply a USB wifi adapter)  You may also consider purchasing a magnetic reed switch if you'd like to know the current status of your garage door (Open/Closed) while remote

2) Make sure Python (& Modules), PHP, MySQL, and Apache are Installed

3) Deploy all Files to /var/www/html/ and Make Sure They are Executable (chmod +x)  For optional Door Status alerting, import the MySQL Dump File and Set up Cron

4) Generate a Unique GUID/Token (cat /proc/sys/kernel/random/uuid) and Add to "Token" Variable in index.php

5) Set up Relay, Switch, and Pi's GPIO as Pictured in Screenshot Below (I used Pin 17 for the Relay and 23 for the Switch, So if You Choose Something Else Update the "Pin" Variable in GarageDoor.py and DoorStatus.py)

6) Port Forward Your Router to Make Your Pi on TCP 80 Accessible to the Internet

7) Create an IFTTT.com Applet for Google Assistant With an Outgoing Webhook (GET Request) as Pictured Below, Using your URL (http://YOUR-PUBLIC-IP/API.php?Token=YOUR-GUID-HERE).  Similarly, create an Incoming Webhook for the Magnetic Reed Switch to get an SMS when the door is left open for X minutes.  You can optionally have the script run GarageDoor.py instead to close it automagically.

8) Say "Ok Google, Open the Garage Door" From Anywhere in the World :)  Phase 2 May Include Leveraging the MySQL DB to Display a History of Open / Closed Times and Durations from a Web Browser, as Well as Provide a Visual Button to Click for Triggering the Door.

# Images : 


![Finished Product](https://i.imgur.com/QHwhLrr.jpg)

![GPIO and Relay Layout](https://i.imgur.com/HqlKxyw.jpg)

![Magnetic Reed Switch](https://i.imgur.com/AotSXBc.png)

![IFTTT Applet Recipie](https://i.imgur.com/wWyx5RH.png)

![Using My Voice to Open!](https://i.imgur.com/KPEASWy.png)

![Accidentally Lef the Door Open](https://i.imgur.com/6CLw2tI.png)
