int data;

void setup() {
 
  Serial.begin(9600);
  pinMode(8,OUTPUT);
  digitalWrite(8,LOW);
  Serial.println("seri haberlesme kuruldu");
}

void loop() {
while (Serial.available()){
  data = Serial.read();
}
if(data=='1')
digitalWrite(8,HIGH);

else if(data=='0')
digitalWrite(8,LOW);

}
