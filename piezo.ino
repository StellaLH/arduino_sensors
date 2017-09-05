void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  delay(10000); // 10 second delay before data transfer starts
}

void loop() {
  float piezoADC = analogRead(A0);
  float piezoV = piezoADC / 1024.0 * 3.0;
  String vib = String(piezoADC);
  Serial.println(vib);
  delay(16); //add delay between each data point

}
