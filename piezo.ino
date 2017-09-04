void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  TFTscreen.begin();
  delay(10000); // 10 second delay before data transfer starts
}

void loop() {
  float piezoADC = analogRead(A1);
  float piezoV = piezoADC / 1023.0 * 5.0;
  String vib = String(piezoADC);
  Serial.println(vib);
  delay(50); //quarter second delay between each data point 
  Serial.println(piezoV)
  delay(50);

}
