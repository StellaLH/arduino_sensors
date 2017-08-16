# -*- coding: utf-8 -*-
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
from plotly.plotly import plot, iplot
from plotly.graph_objs import Scatter, Figure, Layout
from datetime import datetime

#import plotly.plotly as py

#setup 
serial_port='/dev/ttyACM0' # check on Arduino IDE which port used
baud_rate=9600
k=[]
l=[]
m=[]
n=[]
o=[]

voltages=[]
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
            print "data saved"
            
        data=np.array(list(csv.reader(open("sensor_data.txt", "rb"), delimiter=","))).astype("float") # open .csv file from folder 
        time_xdata=[]
        xdata=data[-48:,0]
        for q in xdata:
            time_xdata.append(datetime.strptime("%s"%str(int(q)), "%Y%m%d%H%M%S"))
            
        trace1=Scatter(
            x=time_xdata,
            y= data[-48:,1],
            mode='lines+markers',
            name='Temperature 1\n (degrees C)'
        )
        trace2=Scatter(
            x=time_xdata,
            y= data[-48:,2],
            mode='lines+markers',
            name='Temperature 1 Voltage'
        )
        trace3=Scatter(
            x=time_xdata,
            y= data[-48:,3],
            mode='lines+markers',
            name='Temperature 2\n (degrees C)'
            
        )
        trace4=Scatter(
            x=time_xdata,
            y= data[-48:,4],
            mode='lines+markers',
            name='Temperature 2 Voltage'
        )
        trace5=Scatter(
            x=time_xdata,
            y= data[-48:,5],
            mode='lines+markers',
            name=' Relative Humidity\n (%)'
        )
        trace6=Scatter(
            x=time_xdata,
            y= data[-48:,6],
            mode='lines+markers',
            name='Humidity Voltage\n (%)'
        )
        sensortraces=[trace1,trace3, trace5] #for temperature & humidity plot
        voltagetraces=[trace2,trace4,trace6] #for voltages plot
        title='Sensor Temperature'
        plot(sensortraces, auto_open=False, filename='sensor_data.html')
        t.sleep(898.4) #make up to 15 minutes per acquisition
except KeyboardInterrupt:   
    print "\nFinishing acquisition..."
    data=np.array(list(csv.reader(open("sensor_data.txt", "rb"), delimiter=","))).astype("float") # open .csv file from folder 
    time_xdata=[]
    xdata=data[-48:,0]
    for q in xdata:
        time_xdata.append(datetime.strptime("%s"%str(int(q)), "%Y%m%d%H%M%S"))
        
    trace1=Scatter(
        x=time_xdata,
        y= data[-48:,1],
        mode='lines+markers',
        name='Temperature 1\n (degrees C)'
    )
    trace2=Scatter(
        x=time_xdata,
        y= data[-49:,2],
        mode='lines+markers',
        name='Temperature 1 Voltage'
    )
    trace3=Scatter(
        x=time_xdata,
        y= data[-48:,3],
        mode='lines+markers',
        name='Temperature 2\n (degrees C)'
        
    )
    trace4=Scatter(
        x=time_xdata,
        y= data[-48:,4],
        mode='lines+markers',
        name='Temperature 2 Voltage'
    )
    trace5=Scatter(
        x=time_xdata,
        y= data[-48:,5],
        mode='lines+markers',
        name='Humidity'
    )
    trace6=Scatter(
        x=time_xdata,
        y= data[-48:,6],
        mode='lines+markers',
        name='Humidity Voltage\n (%)'
    )
    sensortraces=[trace1,trace3, trace5]  #for temperature & humidity plot
    voltagetraces=[trace2,trace4,trace6] #for voltages plot
    title='Sensor Temperature'
    plot(sensortraces, auto_open=False, filename='sensor_data.html')
         