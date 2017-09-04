void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  TFTscreen.begin();
  delay(10000); // 10 second delay before data transfer starts
}
void loop() {
  float reading = analogRead(A0);
  float voltage = (reading/1024.0)*5.0; //voltage
  float temp = (voltage-0.55)*100.0; //convert to temp
  String volt_t1=String(voltage);
  String temp1=String(temp);
  Serial.println(temp1);
  delay(250); //quarter second delay between each data point 
  Serial.println(volt_t1)
  delay(250);
  
}

