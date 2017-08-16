"""
Created on Thu Jul 27 15:25:11 2017

@author: stella

Data will be sent to serial port in order:
Temperature --> Temeprature Voltage --> Humidity--> Humidity Voltage

However, python script could start at anypoint in cycle
will have to work this out 
"""

#import modules
import serial
import time as t
import csv
import numpy as np
import paho.mqtt.client as mqtt #import the client
import time

#setup 
serial_port='/dev/ttyACM2' # check on Arduino IDE which port used
baud_rate=9600
k=[] #dumps for data when saving to csv
l=[]
m=[]
n=[]
o=[]
voltages=[]

#setup mqtt connection
broker_address="152.78.131.193" #IP address of labbroker.soton.ac.uk
client = mqtt.Client("P1") #create new instance

def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)


#loop acquire data
try:
    print "Starting acquisition..."
    #with open('sensor_data.txt','a') as f:
    print "Acquisition Initiated! \nTo stop data acquisition, press 'Ctrl' + 'C', or press STOP if using Spyder."
    while True:
        with open('sensor_data.txt','a') as f:

            ser=serial.Serial(serial_port, baud_rate)
            #k=append(i)

            
            line=ser.readline()
            line=str(line.decode("utf-8"))
            l=(float(line))

            
            line=ser.readline()
            line=float(line.decode("utf-8"))
            m=(float(line))
            
            line=ser.readline()
            line=float(line.decode("utf-8"))
            n=(float(line))
            
            line=ser.readline()
            line=float(line.decode("utf-8"))
            o=(float(line))
            
            line=ser.readline()
            line=float(line.decode("utf-8"))
            p=(float(line))
            
            line=ser.readline()
            line=float(line.decode("utf-8"))
            q=(float(line))
            
            
            
            time_str=t.strftime("%H%M%S")
            f.write("%s," %time_str) #time stamp
            f.write("%s," %l) #temp1
            f.write("%s," %m) #temp1 votlage
            f.write("%s," %n) #temp2
            f.write("%s," %o) #temp2 voltage
            f.write("%s," %p) #humidity
            f.write("%s" %q) #humidity voltage
            f.write("\n")
            f.close()


            #publish timestamp
            client.on_message=on_message #attach function to callback
            client.connect(broker_address) #connect to broker
            client.loop_start() #start the loop
            client.subscribe("arduino/timestamp")
            print("Publishing message to topic","arduino/timestamp")
            time_str=float(t.strftime("%H%M%S"))
            client.publish("arduino/timestamp",time_str)
            client.loop_stop()            
            
            #publish temperature 1
            client.on_message=on_message #attach function to callback
            client.connect(broker_address) #connect to broker
            client.loop_start() #start the loop
            client.subscribe("arduino/temp1")
            print("Publishing message to topic","arduino/temp1")
            client.publish("arduino/temp1",l)
            client.loop_stop()   
            
            #publish temperature 2
            client.on_message=on_message #attach function to callback
            client.connect(broker_address) #connect to broker
            client.loop_start() #start the loop
            client.subscribe("arduino/temp2")
            print("Publishing message to topic","arduino/temp2")
            client.publish("arduino/temp2",n)
            client.loop_stop()   
            
            #publish humidity    
            client.on_message=on_message #attach function to callback
            client.connect(broker_address) #connect to broker
            client.loop_start() #start the loop
            client.subscribe("arduino/hum")
            print("Publishing message to topic","arduino/hum")
            client.publish("arduino/hum",p)
            client.loop_stop()   
            
        
except KeyboardInterrupt:   
    print "\nFinishing acquisition..."
    
         