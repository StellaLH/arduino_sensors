# arduino_sensors
an Arduino UNO was used with a handful of sensors to monitor the climatic conditions. The Arduino was programmed using the Arduino IDE and data was collected via the serial port using Python

# LCD_temperature.ino
This is the code uploaded onto the Arduino UNO.
The sensor connections are:

TMP36 temperature sensor --> A0

SEN-09196 MEAS vibration sensor --> A1

LM35 temperature sensor --> A3

HS1101LF humidity sensor --> A5

This script also controls a TTF screen to show sensor data.
