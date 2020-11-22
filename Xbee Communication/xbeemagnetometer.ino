//Libraries
#include <Wire.h>  //Wire library used for I2C communication
#include <SPI.h>  //SPI library needed for IMU
#include <SparkFunLSM9DS1.h>  //IMU library

//Pin definitions 
#define magLED 13

//Objects
LSM9DS1 LSM;  //States "imu" is an LSM9DS1 IMU class object

//Variables
String magData;  //string that will be set to hold all of the IMU magnetometer data
float magX; // magnetometer values
float magY;
float magZ;

void setup() { 
  Serial1.begin(9600); //XBEE SERIAL
  Serial.begin(9600);  //begins serial communications that can be used for troubleshooting at a baud rate of 9600.
  Wire.begin(); //initiates wire library for I2C
  //LED pin outputs 
  pinMode(magLED, OUTPUT);
    
  //IMU possible start up error message
  if (LSM.begin() == false) // with no arguments, this uses default addresses (AG:0x6B, M:0x1E) and i2c port (Wire).
  {
    Serial.println("Failed to communicate with LSM9DS1.");  //Prints error message on startup if the IMU is not wired correctly.
  }
  delay(500);
  
  //Prints header everytime on startup
  String headerLOG = "Time(ms), Mag(x), Mag(y), Mag(z)";  //Defines "headerLOG" as a string that contains the inscribed text.
  Serial.print("magData Format");
  Serial.print(",");
  Serial.print(headerLOG);
  Serial.print("\r");
  delay(500);  //waits 500 ms
}


void loop() {
  //IMU loop (gets the new data every loop and redefines the variables and then puts them in the string "magData"
  if (LSM.magAvailable() ){
    LSM.readMag();
  }
  magX = LSM.calcMag(LSM.mx);
  magY = LSM.calcMag(LSM.my);
  magZ = LSM.calcMag(LSM.mz);
  float magVec = sqrt(magX*magX+magY*magY+magZ*magZ);
  
  //Turns on a LED if there is a strong enough magnetic signal
  if(2 < magVec)
  {
    digitalWrite(magLED, HIGH);
  }
  else
  {
    digitalWrite(magLED, LOW);
  }
  magData = String(magX,5) + "," + String(magY,5) + "," + String(magZ,5);

  //Creates the string "dataLOG" and includes the device measurements listed, which is then printed to the serial monitor.
  String dataLOG = String(millis()) + "," + magData;
  Serial1.print("magData");
  Serial1.print(",");
  Serial1.print(dataLOG);
  Serial1.print("\r");
  delay(250);  //waits .25 sec before re-running the loop  
}