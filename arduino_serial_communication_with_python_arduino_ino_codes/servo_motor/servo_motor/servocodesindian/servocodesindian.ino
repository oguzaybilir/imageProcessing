#include <Servo.h>

Servo servomotor;

int target = 0;
int last_position_of_target = 0;
int servopin = 9;


void setup() {
  Serial.begin(9600);
  servomotor.attach(servopin);

}

void loop() {
  Serial.println("0-180 arası bir aci giriniz");
  while(Serial.available()==0) {}
  target = Serial.parseInt();
  Serial.println(target);

  if(target != last_position_of_target and target != 0 )
 {
  last_position_of_target = target;
  delay(1000);
 }
}
