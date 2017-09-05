void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  delay(10000); // 10 second delay before data transfer starts
}
void loop() {
  int reading = analogRead(A0); 
  float voltage = reading * 3.3;
  voltage /= 1024.0;
  float temperatureC = (voltage - 0.5) * 100 ;
  Serial.println(temperatureC);
  delay(1000);  
}

