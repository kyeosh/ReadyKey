#First attempt installation script
#A successful installation script will turn a fresh
# installation of raspbian into a functioning
# readykey device

#step 1: install all necessary dependancies, rclone 4.3 maybe in the apt repository under testing

sudo apt-get update -y
sudo apt-get upgrade -y
sudo bash /home/pi/readykey/depends.sh -y
curl https://rclone.org/install.sh | sudo bash

#step 2: rewrite rc.local to run the program at boot.

#this line is not ideal because it will overwrite any existing rc.local config

sudo cp  /home/pi/readykey/bin/rc.local /etc/rc.local


# this has not been tested but may append the right lines without ovewriting the config
# could possibly break the gps becasue it does not necessarily take the tttyUSB0 address

#cd /etc/
#RC=rc.local

#if grep -q "sudo /home/pi/readykey/tmu.sh &" "$RC";
#	then
#		echo "File /etc/rc.local already configured. Doing nothing."
#	else
#		sed -i -e "s/^exit 0sudo service gpsd stop & \&\n&/g" "$RC"
#		sed -i -e "s/^exit 0sudo gpsd -N -D3 -F /var/run/gpsd.sock /dev/ttyUSB0 & \&\n&/g" "$RC"
#		sed -i -e "s/^exit 0sudo /home/pi/readykey/tmu.sh & \&\n&/g" "$RC"
#		echo "File /etc/rc.local configured."
#fi

#step 3: request a Bluetooth mac address from the user and save it as KeyID file

read -p "Please enter the MAC address of the bluetooth beacon:" input
echo $input>/home/pi/readykey/KeyID

#step 4: run the rclone configuration script
#currently must run be configured over vnc or with a display to log in to google drive via a browser
# install raspberrypi-ui-mods and chromium-browser to raspian lite before running this script

read -r -p "Do you want to configure rclone to sync location logs to Google Drive? [y/N] " response
if [[  "$response" =~ ^([yY][eE][sS]|[yY])+$ ]]
then 
	read -r -p "You will need a graphical web browser ready on this device for secure login. "
	read -r -p "Do you have a desktop environment and browser running on this device? [y/N] " response
	if [[ "$response" =~ ^([yY][eE][sS]|[yY])+$ ]]
	then
   		rclone config create cloud drive
#step 5: configure crontab to run rclone every 15 mins. check the second answer
#  https://stackoverflow.com/questions/8579330/appending-to-crontab-with-a-shell-script-on-ubuntu 
		#crontab -r   # this line erases crontab, not ideal unless installed on fresh raspbian lite
    		(crontab -l ; echo "0,15,30,45 * * * * /home/pi/readykey/logsync.sh")| crontab -
    		(crontab -l ; echo "0 1 * * * sudo find /home/pi/readykey/log/ -mtime +7 -type f -delete")| crontab -
    		(crontab -l ; echo "0 3 * * * sudo reboot")| crontab -
	else
		read -r -p "Please install a desktop and browser, or configure rclone manaully."
		read -r -p "This program was tested on raspberrypi-ui-mods with chromium-browser."
		exit
	fi
else
	read -r -p "All other cloud storage providers must be configured manually. "
	exit
fi
