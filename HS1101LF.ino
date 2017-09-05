void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  delay(10000); // 10 second delay before data transfer starts
}

void loop() {
  float value = analogRead(A5);
  float humidity=-0.15*value+100.0;
  String volt_h=String (value);
  String hum= String(humidity);
  Serial.println(hum);
  delay(250); //quarter second delay between each data point 
  Serial.println(volt_h);
  delay(250);
  
}
