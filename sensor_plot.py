# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 12:26:09 2017

@author: stella
"""
import serial
import time as t
import csv
import numpy as np
from plotly.offline import plot, iplot
from plotly.graph_objs import Scatter, Figure, Layout
from datetime import datetime

import matplotlib.pyplot as plt

t1=0
t1v=0
t2=0
t2v=0
h=0
hv=0
grapher=0

data_t1=np.array(list(csv.reader(open("t1_sensor_data.txt", "rb"), delimiter=","))).astype("float") # open .csv file from folder
data_t2=np.array(list(csv.reader(open("t2_sensor_data.txt", "rb"), delimiter=","))).astype("float")
data_h1=np.array(list(csv.reader(open("h1_sensor_data.txt", "rb"), delimiter=","))).astype("float")
data_v1=np.array(list(csv.reader(open("v1_sensor_data.txt", "rb"), delimiter=","))).astype("float")


time_xdata=[]
xdata_t1=data_t1[:,0]
xdata_t2=data_t1[:,0]
xdata_h1=data_h1[:,0]


while grapher !='pyplot' and grapher != 'plotly':
    grapher=raw_input("Please choose a grapher: plotly or pyplot?\n")
points=input("How many data points would you like to see?(Max. = %s)\n" %data.shape[0])
while t1!='y'and t1!='n':
    t1=raw_input("Would you like to view temperature 1? [y/n]\n")
while t1v!='y'and t1v!='n':
    t1v=raw_input("Would you like to view temperature 1 voltages? [y/n]\n")
while t2!='y'and t2!='n':
    t2=raw_input("Would you like to view temperature 2? [y/n]\n")
while t2v!='y'and t2v!='n':
    t2v=raw_input("Would you like to view temperature 2 voltages? [y/n]\n")
while h!='y'and h!='n':
    h=raw_input("Would you like to view relative humidity? [y/n]\n") 
while hv!='y'and hv!='n':
    hv=raw_input("Would you like to view relative humidity voltages? [y/n]\n") 
for q in xdata_t1:
    time_xdata_t1.append(datetime.strptime("%s"%str(int(q)), "%Y%m%d%H%M%S"))
for r in xdata_t2:
    time_xdata_t2.append(datetime.strptime("%s"%str(int(q)), "%Y%m%d%H%M%S"))
for s in xdata_h1:
    time_xdata_h1.append(datetime.strptime("%s"%str(int(q)), "%Y%m%d%H%M%S"))


if grapher == 'pyplot':
    pytrace1=data_t1[points*-1:,1]
    pytrace2=data_t1[points*-1:,2]
    pytrace3=data_t2[points*-1:,1]
    pytrace4=data_t2[points*-1:,2]
    pytrace5=data_h1[points*-1:,1]
    pytrace6=data_h1[points*-1:,2]
    
    if t1=='y':
        plt.plot(time_xdata[points*-1:],pytrace1, label="Temp 1")
    else:
        pass
    if t1v=='y':
        plt.plot(time_xdata[points*-1:],pytrace2, label ="Temp 1 Voltages")
    else:
        pass
    if t2=='y':
        plt.plot(time_xdata[points*-1:],pytrace3, label="Temp 2")
    else:
        pass
    if t2v=='y':
        plt.plot(time_xdata[points*-1:],pytrace4, label="Temp 2 Voltages")
    else:
        pass
    if h=='y':
        plt.plot(time_xdata[points*-1:],pytrace5, label="Humidity")
    else:
        pass
    if hv=='y':
        plt.plot(time_xdata[points*-1:],pytrace6, label= "Humidity Voltages")
    else:
        pass   
    plt.legend(bbox_to_anchor=(0.5, 1),loc=8, ncol=2
    )
    plt.show()
    
elif grapher=='plotly':
    sensortraces=[]
    if t1=='y':
        trace1=Scatter(
        x=time_xdata_t1[points*-1:],
        y= data[points*-1:,1],
        mode='lines+markers',
        name='Temperature 1\n (degrees C)'
    )
        sensortraces.append(trace1)
    else:
        pass
    if t1v=='y':
        trace2=Scatter(
        x=time_xdata_t1[points*-1:],
        y= data[points*-1:,2],
        mode='lines+markers',
        name='Temperature 1 Voltage'
    )
        sensortraces.append(trace2)
    else:
        pass
    if t2=='y':
        trace3=Scatter(
        x=time_xdata_t2[points*-1:],
        y= data[points*-1:,3],
        mode='lines+markers',
        name='Temperature 2\n (degrees C)'
    
    )
        sensortraces.append(trace3)
    else:
        pass
    if t2v=='y':
        trace4=Scatter(
        x=time_xdata_t2[points*-1:],
        y= data[points*-1:,4],
        mode='lines+markers',
        name='Temperature 2 Voltage'
    )
        sensortraces.append(trace4)
    else:
        pass
    if h=='y':
        trace5=Scatter(
        x=time_xdata_h1[points*-1:],
        y= data[points*-1:,5],
        mode='lines+markers',
        name='Humidity'
    )
        sensortraces.append(trace5)
    else:
        pass
    if hv=='y':
        trace6=Scatter(
        x=time_xdata_h1[points*-1:],
        y= data[points*-1:,6],
        mode='lines+markers',
        name='Humidity Voltage\n (%)'
    )
        sensortraces.append(trace6)
    else:
        pass   
  
    
    title='Sensor Temperature'
    plot(sensortraces, auto_open=True, filename='sensor_data.html')
    
else:
    print "Please chose a graphing option given in the menu"
