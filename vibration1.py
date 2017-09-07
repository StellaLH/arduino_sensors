# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 17:18:37 2017

@author: stella
"""

import serial
import time as t
import numpy as np
import paho.mqtt.client as mqtt #import the client

#setup 
serial_port='/dev/ttyACM2' # check on Arduino IDE which port used
baud_rate=9600

pulse=[]
pulse_time=[]
means=[]
mins=[]
maxs=[]

#setup MQTT connection
broker_address="labbroker.soton.ac.uk" #IP address of labbroker.soton.ac.uk
client = mqtt.Client("P1") #create new instance

def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)

"""
Read data from serial
""" 
ser=serial.Serial(serial_port, baud_rate)
           
"""
Get average pulse
"""
print "Acquring calibration pulse..."
while len(maxs)<10:

    
    """
    * Get 2 adjacent data points (a & b)
    
    * While difference between the 2 is more
      than 0.5, append first point to pulse array
      
    * When difference is less than 0.5,
      pulse must be over so stop and study
      
    """
    line=ser.readline()
    line1=str(line.decode("utf-8"))
    while len(line1)!= 8.0 and len(line1)!=7.0 and len(line1)!=6.0:
        line=ser.readline()
        line1=str(line.decode("utf-8"))
    a=(float(line1))
    
    
    line=ser.readline()
    line1=str(line.decode("utf-8"))
    while len(line1)!= 8.0 and len(line1)!=7.0 and len(line1)!=6.0:
        line=ser.readline()
        line1=str(line.decode("utf-8"))
    b=(float(line1))
        
    
    if abs(a-b)>2.0:
        while abs(a-b)>2.0:
            print "PULSE!"
            pulse.append(a)
            pulse.append(b)
            line=ser.readline()
            line1=str(line.decode("utf-8"))
           
            while len(line1)!= 8.0 and len(line1)!=7.0 and len(line1)!=6.0:
                line=ser.readline()
                line1=str(line.decode("utf-8"))
            a=(float(line1))
            
            line=ser.readline()
            line1=str(line.decode("utf-8"))
            while len(line1)!= 8.0 and len(line1)!=7.0 and len(line1)!=6.0:
                line=ser.readline()
                line1=str(line.decode("utf-8"))
            b=(float(line1))
        print "Pulse length", len(pulse)
        means.append(np.mean(pulse))
        mins.append(np.min(pulse))
        maxs.append(np.max(pulse))
        pulse=[]
        print "no. calib pulses", len(maxs)
    else:
        pass

    


    
std_mean=np.std(means)
std_min=np.std(mins)
std_max=np.std(mins)

print "Calibration pulse acquired"


#loop acquire data
try:
    print "Starting acquisition of vibration..."
    print "Acquisition Initiated! \nTo stop data acquisition, press 'Ctrl' + 'C', or press STOP if using Spyder."
    while True:
        with open('v1_sensor_data.txt','a') as f:
            
            
            """
            Collect pulses
            """
            pulse=[]
            pulse_time=[]
            line=ser.readline()
            
            """
            * Get 2 adjacent data points
            
            * While difference between the 2 is more
              than 0.5, append first point to pulse array
              
            * When difference is less than 0.5,
              pulse must be over so stop and study
              
            """
            line=ser.readline()
            time_str_a=t.strftime("%Y%m%d%H%M%S")
            line1=str(line.decode("utf-8"))
            while len(line1)!= 8.0 and len(line1)!=7.0 and len(line1)!=6.0:
                line=ser.readline()
                line1=str(line.decode("utf-8"))
            a=(float(line1))
            
            
            line=ser.readline()
            time_str_b=t.strftime("%Y%m%d%H%M%S")
            line1=str(line.decode("utf-8"))
            while len(line1)!= 8.0 and len(line1)!=7.0 and len(line1)!=6.0:
                line=ser.readline()
                line1=str(line.decode("utf-8"))
            b=(float(line1))
                
            while len(pulse)<1:
                if abs(a-b)>2.0:
                    while abs(a-b)>2.0:
                        print "PULSE!"
                        pulse.append(a)
                        pulse.append(b)
                        pulse_time.append(time_str_a)
                        pulse_time.append(time_str_b)
                        line=ser.readline()
                        line1=str(line.decode("utf-8"))
                       
                        while len(line1)!= 8.0 and len(line1)!=7.0 and len(line1)!=6.0:
                            line=ser.readline()
                            line1=str(line.decode("utf-8"))
                        a=(float(line1))
                        
                        line=ser.readline()
                        line1=str(line.decode("utf-8"))
                        while len(line1)!= 8.0 and len(line1)!=7.0 and len(line1)!=6.0:
                            line=ser.readline()
                            line1=str(line.decode("utf-8"))
                        b=(float(line1))
                else: 
                    line=ser.readline()
                    line1=str(line.decode("utf-8"))
                    while len(line1)!= 8.0 and len(line1)!=7.0 and len(line1)!=6.0:
                        line=ser.readline()
                        line1=str(line.decode("utf-8"))
                    a=(float(line1))
                    
                    
                    line=ser.readline()
                    line1=str(line.decode("utf-8"))
                    while len(line1)!= 8.0 and len(line1)!=7.0 and len(line1)!=6.0:
                        line=ser.readline()
                        line1=str(line.decode("utf-8"))
                    b=(float(line1))                    
                        
            
            if (abs(np.mean(pulse)-np.mean(means))>np.std(means)) or (abs(np.min(pulse)-np.min(mins))>np.std(mins)) or (abs(np.max(pulse)-np.max(maxs))>np.std(maxs)): 
                #sends and saves pulse data in mean, min or max of pulse is outside 1 standard deviation
                
                """
                Send time of pulse
                """   
                time_str=t.strftime("%d/%m/%Y %H:%M:%S")
                client.on_message=on_message #attach function to callback
                client.connect(broker_address) #connect to broker
                client.loop_start() #start the loop
                print("Publishing message to topic",time_str,"/xnig/sensors/vib1/time") # topic /xning/sensors/vib1/time
                client.publish("/xnig/sensors/vib1/time",time_str)
                client.loop_stop() 
                
                client.on_message=on_message #attach function to callback
                client.connect(broker_address) #connect to broker
                client.loop_start() #start the loop
                print("Publishing message to topic",np.mean(pulse),"/xnig/sensors/vib1/mean") # topic /xning/sensors/vib1/time
                client.publish("/xnig/sensors/vib1/mean",np.mean(pulse))
                client.loop_stop() 
                 
                
                for i in range(len(pulse)):    
                    f.write("%s," %pulse_time[i])
                    f.write("%s\n" %pulse[i])
                pulse=[]
                pulse_time=[]
            else: #doesn't save pulse if mean, min and max are within 1 standard deviation
                pulse=[]
                pulse_time=[]
            
except KeyboardInterrupt:   
    print "\nFinishing acquisition..."           
            
