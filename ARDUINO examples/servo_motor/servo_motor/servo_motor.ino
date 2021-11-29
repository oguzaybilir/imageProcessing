#include <Servo.h>

Servo servo; // servo controller (multiple can exist)

int servo_pin = 9; // PWM pin for servo control
int pos = 0;    // servo starting position
int input = Serial.parseInt();

void setup() {
  servo.attach(servo_pin); // start servo control
  Serial.begin(9600); // start serial monitor
  Serial.setTimeout(20000); 
  
  servo.write(pos); // move servo to 0 degrees
  Serial.println("Positioned at 0 Degrees");
  Serial.println("Input Desired Angle and Press Enter");
}

void loop() {
  while (Serial.available()){
    String in_char = Serial.readStringUntil('\n'); // read until the newline
    Serial.print("Moving to: ");
    Serial.print(in_char);
    Serial.println(" Degrees");
    servo.write(in_char.toInt()); // convert angle and write servo
    delay(10); // delay for maximum speed
  }
}
