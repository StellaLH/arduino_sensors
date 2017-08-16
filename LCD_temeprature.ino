#include <ThingSpeak.h>


#include <SPI.h>
#include <TFT.h>
#define cs   10
#define dc   9
#define rst  8  

TFT TFTscreen = TFT(cs, dc, rst);
char temp1Printout[6];
char temp2Printout[6];
char temp1voltPrintout[6];
char temp2voltsPrintout[6];
char vibPrintout[6];
char humPrintout[6];
char humvoltPrintout[6];

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  TFTscreen.begin();

  TFTscreen.background(0,0,0);

  TFTscreen.stroke(255,255,255);
  TFTscreen.setTextSize(1);
  TFTscreen.text("Temperature 1\n (degrees C): ",5,5);
  TFTscreen.text("Temperature 2\n (degrees C): ",5,30);
  TFTscreen.text("Relative\n Humidity(%): ",5,55); 
  TFTscreen.setTextSize(1);
  TFTscreen.text("by Stella", 100, 120);
  delay(10000);
}

void loop() {
  // put your main code here, to run repeatedly:
  
  //Temp 1 + voltage
  float reading = analogRead(A0);//get data from pin 0
  float voltage = reading * 5.0; // convert to voltage
  voltage /= 1024.0;
  float temperatureC = (voltage - 0.5) * 100 ;// convert volts to celcius
  String volt_t1=String(reading);
  String temp1=String(temperatureC);
  
  // Temp 2 + voltage
  float voltage2 = analogRead(A3);
  float temperature2 = voltage2/1024.0*500.0;
  String volt_t2=String(voltage2);
  String temp2 = String(temperature2);

  // Humidity + voltage
  float value = analogRead(A4);
  float humidity=-0.15*value+100.0;
  String volt_h=String (value);
  String hum= String(humidity);

  
  //float piezoADC = analogRead(A1);
  //float piezoV = piezoADC / 1023.0 * 5.0;
  //String vib = String(piezoADC);
  
  // Send temp1, temp1 voltage, temp 2, temp2 voltage,
  // Humidty & Humidity Voltage to serial port
  delay(100);
  Serial.println(temp1);
  delay(100); 
  Serial.println(volt_t1);
  delay(100);
  Serial.println(temp2);
  delay(100); 
  Serial.println(volt_t2);
  delay(100); 
  Serial.println(hum);
  delay(100);
  Serial.println(volt_h);
  
  
  temp1.toCharArray(temp1Printout, 5);
  TFTscreen.setTextSize(2);
  TFTscreen.stroke(243,20,180);
  TFTscreen.text(temp1Printout, 90, 5);

  //vib.toCharArray(vibPrintout, 5);
  //TFTscreen.setTextSize(2);
  //TFTscreen.stroke(39,193,247);
  //TFTscreen.text(vibPrintout,90,30);

  temp2.toCharArray(temp2Printout, 5);
  TFTscreen.setTextSize(2);
  TFTscreen.stroke(39,193,247);
  TFTscreen.text(temp2Printout, 90, 30);

  hum.toCharArray(humPrintout, 3);
  TFTscreen.setTextSize(2);
  TFTscreen.stroke(248,178,21);
  TFTscreen.text(humPrintout,90,55);

  //volt_h.toCharArray(hvoltPrintout, 4);
  //TFTscreen.setTextSize(2);
  //TFTscreen.stroke(26,237,105);
  //TFTscreen.text(hvoltPrintout,90,80);

  //temp2.toCharArray(temp2Printout, 5);
  //TFTscreen.setTextSize(2);
  //TFTscreen.stroke(26,237,105);
  //TFTscreen.text(temp2Printout,90,80);
  
  delay(500);
  TFTscreen.stroke(0,0,0);
  TFTscreen.text(temp1Printout, 90, 5);
  //TFTscreen.text(vibPrintout,90,30);
  TFTscreen.text(temp2Printout,90,30);
  TFTscreen.text(humPrintout,90,55);
  //TFTscreen.text(temp2Printout,90,80);
  //TFTscreen.text(hvoltPrintout,90,80);

}
