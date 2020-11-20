/*  Code outputs time elapsed in seconds, temperature Celsius, and temperature Fahrenheit. Output to Serial port
 *   Output as comma separated values.   */
 
#include <Wire.h> // for I2C
int tmp102Address = 0x48;    // I2C address for TMP 102 sensor

void setup(){
    delay(3700); // Delay to give time to output header to serial port
  Serial.begin(9600); // initialize serial port w/ baud rate 9600
  pinMode(35, OUTPUT); //green LED
  pinMode(36, OUTPUT); // yellow LED 
  pinMode(37, OUTPUT); // red LED
  Wire.begin(); //initialize I2C
  Serial.print("Time: "); Serial.print(','); //header
  Serial.print("Celsius: "); Serial.print(',');
  Serial.print("Fahrenheit: "); Serial.println(','); //header, comma separated
  
}

void loop(){
  float celsius = getTemperature();
  Serial.print(millis()/1000); // output time in seconds
  Serial.print(',');
  Serial.print(celsius); // output the temperature celsius
  Serial.print(',');
  float fahrenheit = (1.8 * celsius) + 32; // convert to fahrenheit
  Serial.print(fahrenheit); // output fahrenheit
  Serial.print('.');

  if (fahrenheit <69){
    digitalWrite(35, HIGH); // turn on green LED
    digitalWrite(36, LOW); // yellow off
    digitalWrite(37, LOW); // red off
    }
    else if (fahrenheit <75) {
      digitalWrite(35, LOW); // green off
      digitalWrite(36, HIGH); // turn on yellow LED
      digitalWrite(37, LOW); // red off
      }
     else{
      digitalWrite(35, LOW); // green off
      digitalWrite(36, LOW); // yellow off
      digitalWrite(37, HIGH); //turn on red LED 
     }
     delay(1000); // just heer to slow down the output. You can remove this
}
float getTemperature(){
  Wire.requestFrom(tmp102Address, 2); // code originally from bldr.org
  byte MSB = Wire.read();
  byte LSB = Wire.read();
  // it's a 12bit int, using two's compliment for negative
  int TemperatureSum = ((MSB << 8)| LSB) >> 4;
  float celsius = TemperatureSum *0.0625;
}
