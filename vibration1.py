# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 12:56:21 2017

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


#loop acquire data
try:
    print "Starting acquisition of vibration..."
    print "Acquisition Initiated! \nTo stop data acquisition, press 'Ctrl' + 'C', or press STOP if using Spyder."
    while True:
        with open('v1_sensor_data.txt','a') as f:
	
            """
            Read data from serial
            """ 
            ser=serial.Serial(serial_port, baud_rate)
           
            # Vibration 1 
            line=ser.readline()
            time_str_a=t.strftime("%Y%m%d%H%M%S")
            line1=str(line.decode("utf-8"))
            while len(line1)!= 8.0 and len(line1)!=7.0:
                line=ser.readline()
                line1=str(line.decode("utf-8"))
            a=(float(line1))
        
            line=ser.readline()
            time_str_b=t.strftime("%Y%m%d%H%M%S")
            line1=str(line.decode("utf-8"))
            while len(line1)!= 8.0 and len(line1)!=7.0:
                line=ser.readline()
                line1=str(line.decode("utf-8"))
            b=(float(line1))

            line=ser.readline()
            time_str_c=t.strftime("%Y%m%d%H%M%S")
            line1=str(line.decode("utf-8"))
            while len(line1)!= 8.0 and len(line1)!=7.0:
                line=ser.readline()
                line1=str(line.decode("utf-8"))
            c=(float(line1))

            line=ser.readline()
            time_str_d=t.strftime("%Y%m%d%H%M%S")
            line1=str(line.decode("utf-8"))
            while len(line1)!= 8.0 and len(line1)!=7.0:
                line=ser.readline()
                line1=str(line.decode("utf-8"))
            d=(float(line1))

            line=ser.readline()
            time_str_e=t.strftime("%Y%m%d%H%M%S")
            line1=str(line.decode("utf-8"))
            while len(line1)!= 8.0 and len(line1)!=7.0:
                line=ser.readline()
                line1=str(line.decode("utf-8"))
            e=(float(line1))
            
            if np.std([a,b,c,d,e])>20.0:
                
                f.write("%s," %time_str_a)
                f.write("%s\n" %a)
                f.write("%s," %time_str_b)
                f.write("%s\n" %b)
                f.write("%s," %time_str_c)
                f.write("%s\n" %c)
                f.write("%s," %time_str_d)
                f.write("%s\n" %d)
                f.write("%s," %time_str_e)
                f.write("%s\n" %e)
                
                client.on_message=on_message #attach function to callback
                client.connect(broker_address) #connect to broker
                client.loop_start() #start the loop
                print("Publishing message to topic",a,"/xnig/sensors/vib1")
                client.publish("/xnig/sensors/vib1",a)
                print("Publishing message to topic",b,"/xnig/sensors/vib1")
                client.publish("/xnig/sensors/vib1",b)
                print("Publishing message to topic",c,"/xnig/sensors/vib1")
                client.publish("/xnig/sensors/vib1",c)
                print("Publishing message to topic",d,"/xnig/sensors/vib1")
                client.publish("/xnig/sensors/vib1",d)
                print("Publishing message to topic",e,"/xnig/sensors/vib1")
                client.publish("/xnig/sensors/vib1",e)
                client.loop_stop() 
            else:
                pass
            

except KeyboardInterrupt:   
    print "\nFinishing acquisition..."
