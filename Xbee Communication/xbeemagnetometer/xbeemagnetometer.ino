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

void setupMag()
{
  // [enabled] turns the magnetometer on or off.
  LSM.settings.mag.enabled = true; // Enable magnetometer
  // [scale] sets the full-scale range of the magnetometer
  // mag scale can be 4, 8, 12, or 16
  LSM.settings.mag.scale = 12; // Set mag scale to +/-12 Gs
  // [sampleRate] sets the output data rate (ODR) of the
  // magnetometer.
  // mag data rate can be 0-7:
  // 0 = 0.625 Hz  4 = 10 Hz
  // 1 = 1.25 Hz   5 = 20 Hz
  // 2 = 2.5 Hz    6 = 40 Hz
  // 3 = 5 Hz      7 = 80 Hz
  LSM.settings.mag.sampleRate = 5; // Set OD rate to 20Hz
  // [tempCompensationEnable] enables or disables 
  // temperature compensation of the magnetometer.
  LSM.settings.mag.tempCompensationEnable = false;
  // [XYPerformance] sets the x and y-axis performance of the
  // magnetometer to either:
  // 0 = Low power mode      2 = high performance
  // 1 = medium performance  3 = ultra-high performance
  LSM.settings.mag.XYPerformance = 3; // Ultra-high perform.
  // [ZPerformance] does the same thing, but only for the z
  LSM.settings.mag.ZPerformance = 3; // Ultra-high perform.
  // [lowPowerEnable] enables or disables low power mode in
  // the magnetometer.
  LSM.settings.mag.lowPowerEnable = false;
  // [operatingMode] sets the operating mode of the
  // magnetometer. operatingMode can be 0-2:
  // 0 = continuous conversion
  // 1 = single-conversion
  // 2 = power down
  LSM.settings.mag.operatingMode = 0; // Continuous mode
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
//  Serial.print("magData");
  Serial1.print(",");
//  Serial.print(",");
  Serial1.print(dataLOG);
//  Serial.print(dataLOG);
  Serial1.print("\r");
//  Serial.print("\n");
  delay(100);  //waits .05 sec before re-running the loop  
}
