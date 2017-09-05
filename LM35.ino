void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  TFTscreen.begin();
  delay(10000); // 10 second delay before data transfer starts
}

void loop() {
  float reading2 = analogRead(A3);
  float temperature2 = (reading2/1024.0)*500.0;
  String volt_t2=String(reading2*10.0);
  String temp2 = String(temperature2);
  Serial.println(temp2);
  delay(250); //quarter second delay between each data point 

}
