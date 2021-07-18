import serial
import time

ser = serial.Serial('/dev/ttyACM0',9600)
s = [0,1]
while True:
	read_serial=ser.readline()
	print(read_serial)
	time.sleep(3)