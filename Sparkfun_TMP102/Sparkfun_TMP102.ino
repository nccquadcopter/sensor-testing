#include <SparkFunTMP102.h>

/******************************************************************************
TMP102_example.ino
Example for the TMP102 I2C Temperature Sensor
Alex Wende @ SparkFun Electronics
April 29th 2016
~

This sketch configures the TMP102 temperature sensor and prints the
temperature and alert state (both from the physical pin, as well as by
reading from the configuration register.

Resources:
Wire.h (included with Arduino IDE)
SparkFunTMP102.h

Development environment specifics:
Arduino 1.0+

This code is beerware; if you see me (or any other SparkFun employee) at
the local, and you've found our code helpful, please buy us a round!

Distributed as-is; no warranty is given.   
******************************************************************************/

// Include the SparkFun TMP102 library.
// Click here to get the library: http://librarymanager/All#SparkFun_TMP102

#include <Wire.h> // Used to establied serial communication on the I2C bus
#include <SparkFunTMP102.h> // Used to send and recieve specific information from our sensor

// Connections
// VCC = 3.3V
// GND = GND
// SDA = A4
// SCL = A5
const int ALERT_PIN = A3;

TMP102 sensor0;

void setup() {
  Serial.begin(115200);
  Wire.begin(); //Join I2C Bus

  pinMode(ALERT_PIN,INPUT);  // Declare alertPin as an input

  /* The TMP102 uses the default settings with the address 0x48 using Wire.

     Optionally, if the address jumpers are modified, or using a different I2C bus,
     these parameters can be changed here. E.g. sensor0.begin(0x49,Wire1)

     It will return true on success or false on failure to communicate. */
  if(!sensor0.begin())
  {
    Serial.println("Cannot connect to TMP102.");
    Serial.println("Is the board connected? Is the device ID correct?");
    while(1);
  }

  Serial.println("Connected to TMP102!");
  delay(100);

  // Initialize sensor0 settings
  // These settings are saved in the sensor, even if it loses power

  // set the number of consecutive faults before triggering alarm.
  // 0-3: 0:1 fault, 1:2 faults, 2:4 faults, 3:6 faults.
  sensor0.setFault(0);  // Trigger alarm immediately

  // set the polarity of the Alarm. (0:Active LOW, 1:Active HIGH).
  sensor0.setAlertPolarity(1); // Active HIGH

  // set the sensor in Comparator Mode (0) or Interrupt Mode (1).
  sensor0.setAlertMode(0); // Comparator Mode.

  // set the Conversion Rate (how quickly the sensor gets a new reading)
  //0-3: 0:0.25Hz, 1:1Hz, 2:4Hz, 3:8Hz
  sensor0.setConversionRate(2);

  //set Extended Mode.
  //0:12-bit Temperature(-55C to +128C) 1:13-bit Temperature(-55C to +150C)
  sensor0.setExtendedMode(0);

  //set T_HIGH, the upper limit to trigger the alert on
  sensor0.setHighTempF(82.0);  // set T_HIGH in F
  //sensor0.setHighTempC(29.4); // set T_HIGH in C

  //set T_LOW, the lower limit to shut turn off the alert
  sensor0.setLowTempF(81.0);  // set T_LOW in F
  //sensor0.setLowTempC(26.67); // set T_LOW in C
}

void loop()
{
  float temperature;
  boolean alertPinState, alertRegisterState;

  // Turn sensor on to start temperature measurement.
  // Current consumtion typically ~10uA.
  sensor0.wakeup();

  // read temperature data
  temperature = sensor0.readTempF();
  //temperature = sensor0.readTempC();

  // Check for Alert
  alertPinState = digitalRead(ALERT_PIN); // read the Alert from pin
  alertRegisterState = sensor0.alert();   // read the Alert from register

  // Place sensor in sleep mode to save power.
  // Current consumtion typically <0.5uA.
  sensor0.sleep();

  // Print temperature and alarm state
  Serial.print("Temperature: ");
  Serial.print(temperature);

  Serial.print("\tAlert Pin: ");
  Serial.print(alertPinState);

  Serial.print("\tAlert Register: ");
  Serial.println(alertRegisterState);

  delay(1000);  // Wait 1000ms
}


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
