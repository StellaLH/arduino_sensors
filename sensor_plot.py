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
h1=0
v1=0
grapher=0

data_t1=np.array(list(csv.reader(open("t1_sensor_data.txt", "rb"), delimiter=","))).astype("float") # open .csv file from folder
data_t2=np.array(list(csv.reader(open("t2_sensor_data.txt", "rb"), delimiter=","))).astype("float")
data_h1=np.array(list(csv.reader(open("h1_sensor_data.txt", "rb"), delimiter=","))).astype("float")
data_v1=np.array(list(csv.reader(open("v1_sensor_data.txt", "rb"), delimiter=","))).astype("float")


time_xdata_t1=[]
time_xdata_t2=[]
time_xdata_h1=[]
time_xdata_v1=[]

xdata_t1=data_t1[:,0]
xdata_t2=data_t1[:,0]
xdata_h1=data_h1[:,0]
xdata_v1=data_v1[:,0]


while grapher !='pyplot' and grapher != 'plotly':
    grapher=raw_input("Please choose a grapher: plotly or pyplot?\n")

points=input("-------------------------------------------------\nNumber of data points acquired from each sensor:\ntemperature 1 = %s\ntemperature 2 = %s\nhumidity 1 = %s\nvibration 1 = %s\n\nHow many data points would you like to see?\n" %(len(data_t1), len(data_t2), len(data_h1), len(data_v1)))

while t1!='y'and t1!='n':
    t1=raw_input("-------------------------------------------------\nWould you like to view temperature 1? [y/n]\n")

while t2!='y'and t2!='n':
    t2=raw_input("-------------------------------------------------\nWould you like to view temperature 2? [y/n]\n")

while h1!='y'and h1!='n':
    h1=raw_input("-------------------------------------------------\nWould you like to view humidity 1? [y/n]\n")
        
while v1!='y'and v1!='n':
    v1=raw_input("-------------------------------------------------\nWould you like to view vibration 1? [y/n]\n") 
print "-------------------------------------------------\nYour plot is being processed..."

for q in xdata_t1:
    time_xdata_t1.append(datetime.strptime("%s"%str(int(q)), "%Y%m%d%H%M%S"))

for r in xdata_t2:
    time_xdata_t2.append(datetime.strptime("%s"%str(int(r)), "%Y%m%d%H%M%S"))

for s in xdata_h1:
    time_xdata_h1.append(datetime.strptime("%s"%str(int(s)), "%Y%m%d%H%M%S"))
    
for t in xdata_v1:
    time_xdata_v1.append(datetime.strptime("%s"%str(int(t)), "%Y%m%d%H%M%S"))


if grapher == 'pyplot':
    pytrace1=data_t1[points*-1:,1]

    pytrace3=data_t2[points*-1:,1]

    pytrace5=data_h1[points*-1:,1]
    
    pytrace7=data_v1[points*-1:,1]

    
    if t1=='y':
        plt.plot(time_xdata_t1[points*-1:],pytrace1, label="Temp 1")
    else:
        pass

    if t2=='y':
        plt.plot(time_xdata_t2[points*-1:],pytrace3, label="Temp 2")
    else:
        pass

    if h1=='y':
        plt.plot(time_xdata_h1[points*-1:],pytrace5, label="Humidity")
    else:
        pass
    if v1=='y':
        plt.plot(time_xdata_v1[points*-1:],pytrace7, label="Vibration")
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
        y= data_t1[points*-1:,1],
        mode='lines+markers',
        name='Temperature 1\n (degrees C)'
    )
        sensortraces.append(trace1)
    else:
        pass

    if t2=='y':
        trace3=Scatter(
        x=time_xdata_t2[points*-1:],
        y= data_t2[points*-1:,1],
        mode='lines+markers',
        name='Temperature 2\n (degrees C)'
    
    )
        sensortraces.append(trace3)
    else:
        pass

    if h1=='y':
        trace5=Scatter(
        x=time_xdata_h1[points*-1:],
        y= data_h1[points*-1:,1],
        mode='lines+markers',
        name='Humidity'
    )
        sensortraces.append(trace5)
    else:
        pass
    
    if v1=='y':
        trace7=Scatter(
        x=time_xdata_v1[points*-1:],
        y= data_v1[points*-1:,1],
        mode='lines+markers',
        name='vibration'
    )
        sensortraces.append(trace7)
    else:
        pass

  
    
    title='Sensor Temperature'
    plot(sensortraces, auto_open=True, filename='sensor_data.html')
    
else:
    print "Please chose a graphing option given in the menu"


