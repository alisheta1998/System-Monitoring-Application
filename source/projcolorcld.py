""" 
dht22.py 
Temperature/Humidity monitor using Raspberry Pi and DHT22. 
Data is displayed at thingspeak.com
Original author: Mahesh Venkitachalam at electronut.in 
Modified by Adam Garbo on December 1, 2016 
""" 
import sys 
import RPi.GPIO as GPIO 
from time import sleep 
import Adafruit_DHT 
import urllib.request
import serial
import Adafruit_BMP.BMP085 as BMP085

# urllib.request lib is a dedicated for Python 3 which connect with cloud URL

myAPI = "9FJLRN7H36VLAQWD"
#APIKeys from thingspeak Web site channel

#sensor = BMP085.BMP085()
#sensor_2 = Adafruit_DHT.DHT22
# to identfy the connected Sensors by its version can be considred as objects as it should be downloaded before run 
ser = serial.Serial('/dev/ttyACM0',9600) # to Communicate with ardoino using USB

#pin = 23 # humidty connection with pin 23 
#humidity, temperature = Adafruit_DHT.read_retry(sensor_2, pin)
#temperature2 = sensor.read_temperature()
#pressure = sensor.read_pressure()
#altitude = sensor.read_altitude()
#sealevel = sensor.read_sealevel_pressure()

#thos are a function to collect a data from the sensor DHT22

def main(): 
   print ('starting...') 
   baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI # setup Cloud Connection using your API
   while True: 
       try: # to dont stop the program if Error and go through the next step 
           Red = int(ser.readline())
           sleep(0.5)
           Green = int(ser.readline())
           sleep(0.5)
           Blue  = int(ser.readline())
           sleep(0.5)
           print ( "collect") 
           f = urllib.request.urlopen(baseURL + 
            "&field1=%s&field2=%s&field3=%s" % (Red,Green, Blue)) 
# this Command to Upload the collected data to Cloud channel 
           #print('Temp = {0:0.2f} *C'.format(sensor.read_temperature()))
           #print('Pressure = {0:0.2f} Pa'.format(sensor.read_pressure()))
           #print('Altitude = {0:0.2f} m'.format(sensor.read_altitude()))
           #print('Sealevel Pressure = {0:0.2f} Pa'.format(sensor.read_sealevel_pressure()))
           response = ser.readline()
           print(response)

           #if humidity is not None and temperature is not None:
              #print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
           #else:
              #print('Failed to get reading. Try again!')
              # that Condition to work with temp and H sensor 

           #RH, T = getSensorData() 
           #f = urllib.request.urlopen(baseURL + "&field1=%s&field2=%s" % (RH, T))
           #print ("humidity= "+humidity)
           #print ("Temprature= "+temperature)

           #print (f.read()) 
           #f.close() 
           sleep(1) #uploads DHT22 sensor values every 3 Sec 
       except: 
           print ('exiting.') 
           break 
#call main 
if __name__ == '__main__': 
   main()  
