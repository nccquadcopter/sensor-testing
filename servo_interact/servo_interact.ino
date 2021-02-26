#include <Servo.h> //library for controlling a servo

#define servoPin 2  //pin for the servo
Servo myservo;  // create servo object to control a servo
//int pos = 0;    // variable to store the servo position
//int increment = 1;        // increment to move for each interval
//int ServoUpdateInterval = 15;      // interval between servo updates Modifying this along with increment allows you to adjust the speed. Fine tune these to avoid choppy motion.
int received = 0;

void setup() {
  Serial.begin(9600); 
  Serial1.begin(9600); 
}
 
void loop() {
  if (Serial.available() > 0) {
received = Serial.read();
    if (received == 'a'){
    myservo.attach(servoPin);
    myservo.write(0);
    delay(2000);
    myservo.write(120);
    }
     else if (received == 'b'){
      myservo.detach();
     }
    }
  } 


//void loop() {
//  //Servo loop
//  if(magnet==true){ //snaps the servo to its middle position if a magnetic signal is detected
//    pos = 90;
//    myservo.write(pos);
//  }
//  else if((millis() - lastServoUpdate) > ServoUpdateInterval){ //moves the servo back and forth if there is no magnet
//    lastServoUpdate = millis();
//    pos += increment;
//    myservo.write(pos);
//    Serial.println(pos);
//    if ((pos >= 180) || (pos <= 0)) // end of sweep
//    {
//      // reverse direction
//      increment = -increment;
//    }
//  }
