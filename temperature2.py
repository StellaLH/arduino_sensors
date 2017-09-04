# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 12:52:40 2017

@author: stella
"""
#import modules
import serial
import time as t
import csv
import numpy as np
import paho.mqtt.client as mqtt #import the client
import time

#setup 
serial_port='/dev/ttyUSB0' # check on Arduino IDE which port used
baud_rate=9600

#setup MQTT connection
broker_address="labbroker.soton.ac.uk" #IP address of labbroker.soton.ac.uk
client = mqtt.Client("P1") #create new instance

def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)


#loop acquire data
try:
    print "Starting acquisition of temperature 2..."
    print "Acquisition Initiated! \nTo stop data acquisition, press 'Ctrl' + 'C', or press STOP if using Spyder."
    while True:
        with open('t2_sensor_data.txt','a') as f:
	
            """
            Read data from serial
            """ 
            ser=serial.Serial(serial_port, baud_rate)
           
            #Temperature 2 
            line=ser.readline()
            line=str(line.decode("utf-8"))
            l=(float(line))
		
            #Temperature 2 Voltage	
            line=ser.readline()
            line=float(line.decode("utf-8"))
            m=(float(line))
            
            """
            Save serial data to CSV
            """
            time_str=t.strftime("%Y%m%d%H%M%S")
            f.write("%s," %time_str) #time stamp
            f.write("%s," %l) #temp2
            f.write("%s," %m) #temp2 votlage
            
            """
            Publish data to MQTT
            """          
            #publish temperature 2
            client.on_message=on_message #attach function to callback
            client.connect(broker_address) #connect to broker
            client.loop_start() #start the loop
            print("Publishing message to topic",l,"/xnig/sensors/temp2")
            client.publish("/xnig/sensors/temp2",l)
            client.loop_stop()   

except KeyboardInterrupt:   
    print "\nFinishing acquisition..."