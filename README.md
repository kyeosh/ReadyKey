# Kyeocycle
This repository contains a set of programs designed to run on a Raspberry Pi. The main function of the code is to detect a Bluetooth beacon and trigger relays. I use it as a key. allowing me to start a vehicle. The secondary function is GPS tracking.  This code will poll gpsd and save the location to a .csv log file. As long as the Raspberry Pi has an internet connection you can use rclone to upload a record of the saved locations. 

The "tmu.sh" is intended to be started at boot by adding:

     sudo /home/pi/kyeocycle/tmu.sh &

to the rc.local file. 

The gpsd code is sometimes finnicky so it useful to add:

    sudo service gpsd stop
 
    sudo gpsd -N -D3 -F /var/run/gpsd.sock /dev/ttyUSB0 &
 
 to rc.local as well.
 
Logging to a cloud folder can be set up by adding:
 
    0,15,30,45 * * * * /home/pi/kyeocycle/logsync.sh
  
     0 1 * * * sudo find /home/pi/kyeocycle/log/ -mtime +7 -type f -delete
  
     0 3 * * * sudo reboot
  
 to crontab. The reboot is necessary to set a new log name everyday. Otherwise the syncing process would take more data each time. this way it seems to use the same amount everyday.


The "simpler" folder is older versions of the core python script, without some features included in the final version.

The detectall.py  code is meant to to be installed on a Raspberry Pi to accutate relays when a Bluetooth (BLE) beacon is detected.

The detectallkey.py code does the same thing but waits for an input on GPIO 38 . If an input is detected, the program activates the relays if not the program waits for the bluetooth beacon.  

The gpskeydetect.py code adds a GPS location line to the output, this allows live monitoring over ssh. I run it in tmux accessibiltiy

The gpslog.py codes adds a simple text log output, which can be synced to a cloud folder using rclone. This is done by adding a reference to "logsync.sh" to crontab. Early version of rclone will not allow the "--ignore-checksum" flag so be sure you are using the newest version. The version in the apt repository was not updated when I wrote this code and I needed to install rclone manually.

