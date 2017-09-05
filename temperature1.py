# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 12:43:15 2017

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
serial_port='/dev/ttyUSB1' # check on Arduino IDE which port used
baud_rate=9600

#setup MQTT connection
broker_address="labbroker.soton.ac.uk" #IP address of labbroker.soton.ac.uk
client = mqtt.Client("P1") #create new instance

def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)

i=0 
#loop acquire data
try:
    print "Starting acquisition of temperature 1..."
    print "Acquisition Initiated! \nTo stop data acquisition, press 'Ctrl' + 'C', or press STOP if using Spyder."
    while True:
        with open('t1_sensor_data.txt','a') as f:
                       
            if i==60: #only saves to CSV once every minute
                """
                Read data from serial
                """ 
                ser=serial.Serial(serial_port, baud_rate)
               
                #Temperature 1 
                line=ser.readline()
                line1=str(line.decode("utf-8"))
                while len(line1)!= 7.0 and len(line1)!=6.0:
                    line=ser.readline()
                    line1=str(line.decode("utf-8"))
                l=(float(line1))
    		           
                """
                Save serial data to CSV
                """
                time_str=t.strftime("%Y%m%d%H%M%S")
                f.write("%s," %time_str) #time stamp
                f.write("%s\n" %l) #temp1
                
                """
                Publish data to MQTT
                """
                
                #publish timestamp
                client.on_message=on_message #attach function to callback
                client.connect(broker_address) #connect to broker
                client.loop_start() #start the loop
                time_str=float(t.strftime("%H%M%S"))
                print("Publishing message to topic",time_str,"/xnig/sensors/timestamp")
                client.publish("/xnig/sensors/timestamp",time_str)
                client.loop_stop()           
                
                #publish temperature 1
                client.on_message=on_message #attach function to callback
                client.connect(broker_address) #connect to broker
                client.loop_start() #start the loop
                print("Publishing message to topic",l,"/xnig/sensors/temp1")
                client.publish("/xnig/sensors/temp1",l)
                client.loop_stop()
                i=0
            
            else:
                """
                Read data from serial
                """ 
                ser=serial.Serial(serial_port, baud_rate)
               
                #Temperature 1 
                line=ser.readline()
                line1=str(line.decode("utf-8"))
                while len(line1)!= 7.0 and len(line1)!=6.0:
                    line=ser.readline()
                    line1=str(line.decode("utf-8"))
                l=(float(line1))
                
                """
                Publish data to MQTT
                """    
                
                #publish timestamp
                client.on_message=on_message #attach function to callback
                client.connect(broker_address) #connect to broker
                client.loop_start() #start the loop
                time_str=float(t.strftime("%H%M%S"))
                print("Publishing message to topic",time_str,"/xnig/sensors/timestamp")
                client.publish("/xnig/sensors/timestamp",time_str)
                client.loop_stop()
                
                #publish temperature 1
                client.on_message=on_message #attach function to callback
                client.connect(broker_address) #connect to broker
                client.loop_start() #start the loop
                print("Publishing message to topic",l,"/xnig/sensors/temp1")
                client.publish("/xnig/sensors/temp1",l)
                client.loop_stop()
                
                i+=1
            

except KeyboardInterrupt:   
    print "\nFinishing acquisition..."
