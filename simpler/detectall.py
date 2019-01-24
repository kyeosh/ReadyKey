import bluetooth
import time
import RPi.GPIO as GPIO

#this command sets relay number to correspond with "physical" numbers in the $gpio readall table

GPIO.setmode(GPIO.BOARD)
RELAY1 = 7
RELAY2 = 11
RELAY3 = 12
RELAY4 = 13
RELAY5 = 15
RELAY6 = 16
RELAY7 = 18
RELAY8 = 22 
GPIO.setup(RELAY1, GPIO.OUT)
GPIO.setup(RELAY2, GPIO.OUT)
GPIO.setup(RELAY3, GPIO.OUT)
GPIO.setup(RELAY4, GPIO.OUT)
GPIO.setup(RELAY5, GPIO.OUT)
GPIO.setup(RELAY6, GPIO.OUT)
GPIO.setup(RELAY7, GPIO.OUT)
GPIO.setup(RELAY8, GPIO.OUT)


while True:
	print "Checking " + time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())
	result =  bluetooth.lookup_name('94:65:2d:82:53:61', timeout=60)
	if (result != None):
		print "Tom's here :)"
		GPIO.output(RELAY1,0)
		GPIO.output(RELAY2,0)
		GPIO.output(RELAY3,0)
		GPIO.output(RELAY4,0)
		GPIO.output(RELAY5,0)
		GPIO.output(RELAY6,0)
		GPIO.output(RELAY7,0)
		GPIO.output(RELAY8,0)
		time.sleep(10)
	else:
		print "Tom's gone :("
		GPIO.output(RELAY1,1)
		GPIO.output(RELAY2,1)
		GPIO.output(RELAY3,1)
		GPIO.output(RELAY4,1)
		GPIO.output(RELAY5,1)
		GPIO.output(RELAY6,1)
		GPIO.output(RELAY7,1)
		GPIO.output(RELAY8,1)
		time.sleep(10)
