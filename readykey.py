
import os
from gps import *
from time import *
import logging
import time
import threading
import bluetooth
import  rpi_backlight as bl
import RPi.GPIO as GPIO

logging.basicConfig(filename='/home/pi/readykey/log/'+(time.strftime("%d%b%Y", time.localtime()))+'.csv', level=logging.INFO, format='%(message)s')
logging.info("Status, Time, Latitude, Longitude")

GPIO.setmode(GPIO.BOARD)
RELAY1 = 7
RELAY2 = 11
RELAY3 = 12
RELAY4 = 13
RELAY5 = 15
RELAY6 = 16
RELAY7 = 18
RELAY8 = 22
KEY = 38
GPIO.setup(RELAY1, GPIO.OUT)
GPIO.setup(RELAY2, GPIO.OUT)
GPIO.setup(RELAY3, GPIO.OUT)
GPIO.setup(RELAY4, GPIO.OUT)
GPIO.setup(RELAY5, GPIO.OUT)
GPIO.setup(RELAY6, GPIO.OUT)
GPIO.setup(RELAY7, GPIO.OUT)
GPIO.setup(RELAY8, GPIO.OUT)
GPIO.setup(KEY, GPIO.IN, GPIO.PUD_DOWN)

with open('/home/pi/readykey/KeyID','r') as myfile:
  BEACON = myfile.read()
 
gpsd = None #seting the global variable
 
os.system('clear') #clear the terminal (optional)
 
class GpsPoller(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    global gpsd #bring it in scope
    gpsd = gps(mode=WATCH_ENABLE) #starting the stream of info
    self.current_value = None
    self.running = True #setting the thread running to true
 
  def run(self):
    global gpsd
    while gpsp.running:
      gpsd.next() #this will continue to loop and grab EACH set of gpsd info to clear the buffer
 
if __name__ == '__main__':
  gpsp = GpsPoller() # create the thread
  try:
    gpsp.start() # start it up
    while True:
		tom =  bluetooth.lookup_name(BEACON.rstrip(), timeout=110)
		if ((tom != None) or (GPIO.input(38))):
			while (GPIO.input(38)):	
				GPIO.output(RELAY1,0)
				GPIO.output(RELAY2,0)
				GPIO.output(RELAY3,0)
				GPIO.output(RELAY4,0)
				GPIO.output(RELAY5,0)
				GPIO.output(RELAY6,0)
				GPIO.output(RELAY7,0)
				GPIO.output(RELAY8,0)
				bl.set_power(True)
				time.sleep(10)
				check="Key Engaged, " + time.strftime("%d %b %Y %H:%M:%S", time.localtime()) + ",  " + str(gpsd.fix.latitude) + ",  " + str(gpsd.fix.longitude)
				print(check)
				logging.info(check)
			else:
				if (tom != None):
					GPIO.output(RELAY1,0)
					GPIO.output(RELAY2,0)
					GPIO.output(RELAY3,0)
					GPIO.output(RELAY4,0)
					GPIO.output(RELAY5,0)
					GPIO.output(RELAY6,0)
					GPIO.output(RELAY7,0)
					GPIO.output(RELAY8,0)
					bl.set_power(True)
					time.sleep(10)
					check="Beacon Detected, " + time.strftime("%d %b %Y %H:%M:%S", time.localtime()) + ",  " + str(gpsd.fix.latitude) + ",  " + str(gpsd.fix.longitude)
					print(check)
					logging.info(check)
		else:
			GPIO.output(RELAY1,1)
			GPIO.output(RELAY2,1)
			GPIO.output(RELAY3,1)
			GPIO.output(RELAY4,1)
			GPIO.output(RELAY5,1)
			GPIO.output(RELAY6,1)
			GPIO.output(RELAY7,1)
			GPIO.output(RELAY8,1)
			bl.set_power(False)
			time.sleep(10)
			check="Inactive, " + time.strftime("%d %b %Y %H:%M:%S", time.localtime()) + ",  " + str(gpsd.fix.latitude) + ",  " +  str(gpsd.fix.longitude)
			print(check)
			logging.info(check)
  except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
    print "\nKilling Thread..."
    gpsp.running = False    
  print "Done.\nExiting."
