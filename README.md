# ReadyKey
This repository contains a set of programs designed to run on a Raspberry Pi. The main function of the code is to detect a Bluetooth beacon and trigger relays. I use it as a key. allowing me to start a vehicle. The secondary function is GPS tracking.  This code will poll gpsd and save the location to a .csv log file. As long as the Raspberry Pi has an internet connection you can use rclone to upload a record of the saved locations. 

To install this program simply clone this repository and run the installation script. 
The script it set up to configure rclone to sync log files with the timestamp and coordinates to your google drive account. In order to for this part of the installation to work, you must be using a desktop environment witha browser installed. If you would rather use the bluetooth switching utility without the logging. You can opt out to the rclone and crontab configuration. This will run perfectly fine on raspbian lite headless. The logs will record coordinates as 0, 0.

