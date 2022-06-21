const int POTENTIOMETER_PIN = A0;
const int LED_PIN = 3;
const int ANALOG_THRESHOLD = 500;

void setup() {
  Serial.begin(9600);
  pinMode(LED_PIN,OUTPUT);

}

void loop() {
  int analogValue = analogRead(POTENTIOMETER_PIN);
  Serial.println(analogValue);

  if(analogValue > ANALOG_THRESHOLD){
    digitalWrite(LED_PIN, HIGH);}
  else{
    digitalWrite(LED_PIN, LOW);}
   delay(100);
  
}
