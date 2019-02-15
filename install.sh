#First attempt installation script
#A successful installation script will turn a fresh
# installation of raspbian into a functioning
# readykey device

#step 1: install all necessary dependancies, rclone 4.3 maybe in the apt repository under testing
sudo apt-get update -y
sudo apt-get upgrade -y
sudo bash /home/pi/kyeocycle/depends.sh -y
curl https://rclone.org/install.sh | sudo bash

#step 2: rewrite rc.local to run the program at boot.
sudo cp  /home/pi/kyeocycle/bin/rc.local /etc/rc.local

#step 3: request a Bluetooth mac address from the user and save it as KeyID file
read -p "Please enter the MAC address of the bluetooth beacon:" input
echo $input>/home/pi/kyeocycle/KeyID

#step 4: run the rclone configuration script
#currently must run be configured over vnc or with a display to log in to google drive via a browser
# install raspberrypi-ui-mods and chromium-browser to raspian lite before running this script
rclone config create cloud drive

#step 5: configure crontab to run rclone every 15 mins. check the second answer
#  https://stackoverflow.com/questions/8579330/appending-to-crontab-with-a-shell-script-on-ubuntu  
crontab -r
(crontab -l ; echo "0,15,30,45 * * * * /home/pi/kyeocycle/logsync.sh")| crontab -
(crontab -l ; echo "0 1 * * * sudo find /home/pi/kyeocycle/log/ -mtime +7 -type f -delete")| crontab -
(crontab -l ; echo "0 3 * * * sudo reboot")| crontab -
