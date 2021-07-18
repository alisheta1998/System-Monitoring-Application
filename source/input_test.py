import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.IN)
print ("this program will test an input on pin 12")
while True:
	if(GPIO.input(12)==True):
		print ("input is true 3.3 Volt")
	else:
		print ("input is false (Zero Volt)")
	time.sleep(2)
