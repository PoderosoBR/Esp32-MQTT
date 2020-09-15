from time import sleep
from umqtt.simple import MQTTClient
from machine import Pin
from dht import DHT22
import time 


import network

from network import WLAN 

wlan = WLAN() 

nic = network.WLAN(network.STA_IF)
nic.active(True)
nic.connect('BRUNO', 'samsung1')


SERVER = '192.168.0.42'
CLIENT_ID = 'ESP32_DHT22_Sensor'
TOPIC = b'temp_humidity'



client = MQTTClient(CLIENT_ID, SERVER)
client.connect()

 
while not wlan.isconnected():  
    machine.idle()
    print("DESCONECTADO")
print("Connected to Wifin")


seg = 0
min = 0
hor = 0

while(hor<24):
  #time.sleep(1)
  print(hor , ":",min,":",seg)

  seg+= 1
  if seg == 60:
    min+=1    
    seg=0
  if min == 60:
    hor+=1
    min= 0
    seg = 0
  if min == 10 or min == 25 or min == 33:
      if seg == 0: 
       print(hor , ":",min,":",seg)
       Pin(2,Pin.OUT).value(1)
  else:
        Pin(2,Pin.OUT).value(0)
 
