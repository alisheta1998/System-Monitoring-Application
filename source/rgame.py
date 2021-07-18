import time
import RPi.GPIO as GPIO
import random
Player_1= input("first player name is")
Player_2= input("second player name is")
GPIO.setmode(GPIO.BOARD)
GPIO.setup (19,GPIO.IN)
GPIO.setup (26, GPIO.IN)
GPIO.setup (13, GPIO.OUT)
GPIO.output(13,1)
time.sleep(random.uniform(25,50))
GPIO.output(13,0)
while (GPIO.input(19)==True) and (GPIO.input(26)==True):
	pass
	print ("no inputs")
if GPIO.input(19)==False:
	print(Player_1 + " WON")
if GPIO.input(26)==False:
	print(Player_2 + " WON")
GPIO.cleanup()

