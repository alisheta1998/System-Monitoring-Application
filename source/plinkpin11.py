import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.OUT)
while True:
	GPIO.output(12,0)
	print ("output 0")
	time.sleep(5)
	
	GPIO.output(12,1)
	print (" output 1")
	time.sleep(5)
	

 
