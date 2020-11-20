String readString = "";
//demonstration
void setup() {
  Serial.begin(9600);           //instantiate local serial (the regular usb port)
  Serial1.begin(9600);          //instantiate xbee serial (the teensy transmit/recieve pins 0 and 1)
}
void loop() {
  if (Serial.available() > 0) {
    char c = Serial.read();     //gets one byte from serial buffer
    readString += c;            //append that byte to readString
    if (c == '\n'){             //but, if you detect a new line..take the constructed string and do the following:
    Serial1.print("From Sensor A: "); // tag the sensor so we know which sensor sent this data
    Serial1.print(',');         //add a comma so we can seperate the tag from the data later on
    Serial1.print(readString);  //print in xbee terminal on pc
    Serial1.print('\r');        //add a character that indicattes the end of line
    Serial.print(readString);   //print in local terminal
    readString = "";            //reset our readString variable so it's ready for a new command 
    }
  }
}
