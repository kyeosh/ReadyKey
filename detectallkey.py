import bluetooth
import time
import RPi.GPIO as GPIO

#this command sets relay number to correspond with "physical" numbers in the $gpio readall table
#added key and configure pin # 38 to loook for a 5v signal, i am taking the signal from pin 2 and 
#I plan to use a key switch to open or close the connection

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


#added key detection and restructured the mainloop, moved the checking statement to the after the wait,
#so when it prints checking it will immediately loop back to the check. 

while True:
	tom = bluetooth.lookup_name('94:65:2d:82:53:61', timeout=100)
	if ((tom != None) or (GPIO.input(38))):
		while (GPIO.input(38)):
			print "Key bypass engaged "
			GPIO.output(RELAY1,0)
			GPIO.output(RELAY2,0)
			GPIO.output(RELAY3,0)
			GPIO.output(RELAY4,0)
			GPIO.output(RELAY5,0)
			GPIO.output(RELAY6,0)
			GPIO.output(RELAY7,0)
			GPIO.output(RELAY8,0)
			time.sleep(10)
			print "Checking " + time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())
		else:
			if (tom != None):
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
				print "Checking " + time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())

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
		print "Checking " + time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())
