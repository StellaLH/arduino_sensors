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
    print "Starting acquisition..."
    #with open('sensor_data.txt','a') as f:
    print "Acquisition Initiated! \nTo stop data acquisition, press 'Ctrl' + 'C', or press STOP if using Spyder."
    while True:
        with open('sensor_data.txt','a') as f:
	
            """
            Read data from serial
            """ 
            ser=serial.Serial(serial_port, baud_rate)
           
            #Temperature 1 
            line=ser.readline()
            line=str(line.decode("utf-8"))
            l=(float(line))
		
	    #Temperature 1 Voltage	
            line=ser.readline()
            line=float(line.decode("utf-8"))
            m=(float(line))
            
            #Temperature 2
            line=ser.readline()
            line=float(line.decode("utf-8"))
            n=(float(line))
            
            #Temperature 2 Voltage
            line=ser.readline()
            line=float(line.decode("utf-8"))
            o=(float(line))
            
            #Relative Humidity
            line=ser.readline()
            line=float(line.decode("utf-8"))
            p=(float(line))
            
            #Relative Humidity Voltage
            line=ser.readline()
            line=float(line.decode("utf-8"))
            q=(float(line))
            
            
            """
            Save serial data to .csv
            """
            time_str=t.strftime("%Y%m%d%H%M%S")
            f.write("%s," %time_str) #time stamp
            f.write("%s," %l) #temp1
            f.write("%s," %m) #temp1 votlage
            f.write("%s," %n) #temp2
            f.write("%s," %o) #temp2 voltage
            f.write("%s," %p) #humidity
            f.write("%s" %q) #humidity voltage
            f.write("\n")
            f.close()

            """
            Publish data to MQTT
            """
            #publish timestamp
            client.on_message=on_message #attach function to callback
            #client.username_pw_set("xnigsensors@gmail.com", "03c34bc4")
            client.connect(broker_address) #connect to broker
            client.loop_start() #start the loop
            client.subscribe("xnig/timestamp")
            print("Publishing message to topic","/xnigsensors@gmail.com/xnig/timestamp")
            time_str=float(t.strftime("%H%M%S"))
            client.publish("/xnigsensors@gmail.com/xnig/timestamp",time_str)
            client.loop_stop()            
            
            #publish temperature 1
            client.on_message=on_message #attach function to callback
            #client.username_pw_set("xnigsensors@gmail.com", "03c34bc4")
            client.connect(broker_address) #connect to broker
            client.loop_start() #start the loop
            client.subscribe("xnig/temp1")
            print("Publishing message to topic",l,"/xnigsensors@gmail.com/xnig/temp1")
            client.publish("/xnigsensors@gmail.com/xnig/temp1",l)
            client.loop_stop()   
            
            #publish temperature 2
            client.on_message=on_message #attach function to callback
            #client.username_pw_set("xnigsensors@gmail.com", "03c34bc4")
            client.connect(broker_address) #connect to broker
            client.loop_start() #start the loop
            client.subscribe("xnig/temp2")
            print("Publishing message to topic",n,"/xnigsensors@gmail.com/xnig/temp2")
            client.publish("/xnigsensors@gmail.com/xnig/temp2",n)
            client.loop_stop()   
            
            #publish humidity    
            client.on_message=on_message #attach function to callback
            #client.username_pw_set("xnigsensors@gmail.com", "03c34bc4")
            client.connect(broker_address) #connect to broker
            client.loop_start() #start the loop
            client.subscribe("xnig/hum")
            print("Publishing message to topic",p,"/xnigsensors@gmail.com/xnig/hum")
            client.publish("/xnigsensors@gmail.com/xnig/hum",p)
            client.loop_stop()   
            
#            time.sleep(20)
            
        
except KeyboardInterrupt:   
    print "\nFinishing acquisition..."
    
         
