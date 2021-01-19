//Code from: https://create.arduino.cc/projecthub/infoelectorials/project-009-arduino-temt6000-light-sensor-project-5349d7#tools

int temt6000Pin = 0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  int value = analogRead(temt6000Pin);
  Serial.print("Ambient Light Reading: ");
  Serial.print(value);
  Serial.println(" Lux");
  delay(1000);
}
