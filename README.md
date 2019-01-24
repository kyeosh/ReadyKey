# Kyeocycle
This repository contains a set of programs designed to run on a Raspberry Pi. The main function of the code is to detect a Bluetooth beacon and trigger relays. I use it as a key. allowing me to start a vehicle. The secondary function is GPS tracking.  This code will poll gpsd and save the location to a .csv log file. As long as the Raspberry Pi has an internet connection you can use rclone to upload a record of the saved locations. 

The "simpler" folder is older versions of the core python script, without some features included in the final version.

The detectall.py  code is meant to to be installed on a Raspberry Pi to accutate relays when a Bluetooth (BLE) beacon is detected.

The detectallkey.py code does the same thing but waits for an input on GPIO 38 . If an input is detected, the program activates the relays if not the program waits for the bluetooth beacon.  
