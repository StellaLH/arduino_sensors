# arduino_sensors
an Arduino UNO was used with a handful of sensors to monitor the climatic conditions. The Arduino was programmed using the Arduino IDE and data was collected via the serial port using Python.

Before running temp_hum_volts_nodered.py, in the same directory, make sure there is an empty file called sensor_data.txt to save the sensor data to.

# LCD_temperature.ino ==> for sensors connected to a single Arduino
This is the code uploaded onto the Arduino UNO.
The sensor connections are:

TMP36 temperature sensor --> A0

SEN-09196 MEAS vibration sensor --> A1

LM35 temperature sensor --> A3

HS1101LF humidity sensor --> A5

This script also controls a TTF screen to show sensor data.
By un-commenting sections, different sensor values can be displayed on the TTF screen and specific sensor and voltage values can also be sent via the serial port.

# temp_hum_volts_plotly.py ==> for sensors connected to a single Arduino

Acquires data from the 2 temperature sensors and the humidity sensor, then sends to Plotly.

Make and pltoly accounts and configure with python on your computer, then you are able to embed the graphs onto webpages. For example, view our sensor data webpage https://xnig.wordpress.com/temperature-humidity-sensors/

# temp_hum_volts_nodered.py ==> for sensors connected to a single Arduino

Acquires data from the 2 temperature sensors and the humidity sensor, then publishes the data through a data broker to node-red. 

# nodered_flow ==> for sensors connected to a single Arduino

Once you have installed node red and have the GUI open on a browser, copy this script to your clipboard and select  menu,import,clipboard,past,import on the Node-RED editor. Hit deploy and open the dashboard to see sensor data displayed dynamically.

# current_sensor

Arduino sketch for non-inasive current sensor.

When using the current clamp,  ensure a scaling ccircuit is used to scale the output voltages between 0V and +5V. The circuit to do so is in the report, but the 2 x 10kOhm resistors can be increased if a very small current is used. The 33kOhm resisor is just to stop static between the wires. The capacitor is just for reducing noise, whilst prototyping, consider changing / removing. 

After setting up the circuit, upload the current_sensor sketch to the Arduino.

# TMP36.ino ==> for single temperature sensor
Arduino sketch when you connect a single TMP36 temperature sensor to the Arduino.
# LM35.ino  ==> for single temperature sensor
Arduino sketch when you connect a single LM35 temperature sensor to the Arduino.
# HS1101LF.ino  ==> for single relative humidity sensor
Arduino sketch when you connect a single HS1101LF relative humidity sensor to the Arduino.
# piezo.ino  ==> for single vibration sensor
Arduino sketch when you connect a single MEAS SEN-09196 piezo vibration sensor to the Arduino.

# temperature1.py
Script to send TMP36 sensor data to Node-RED over topic /xnig/sensors/temp1, and timestamps to topic /xnig/sensors/timestamp.
Ensure there is a file called t1_sensor_data.txt in the same directory as this script.


# temperature1.py
Script to send LM35 sensor data to Node-RED over topic /xnig/sensors/temp2.
Ensure there is a file called t2_sensor_data.txt in the same directory as this script.


# humidity1.py
Script to send HS1101LF sensor data to Node-RED over topic /xnig/sensors/hum1.
Ensure there is a file called h1_sensor_data.txt in the same directory as this script.


# vibration1.py
Script to send piezo vibration sensor data to Node-RED over topic /xnig/sensors/vib1.
Ensure there is a file called v1_sensor_data.txt in the same directory as this script.


