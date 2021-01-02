#include <Servo.h> 

Servo myservo;

int edasi = 1600;
int tagasi = 1400;

void setup() {
  
  myservo.attach(11);
  
  Serial.begin(9600); 

}

void loop() {
  
 myservo.writeMicroseconds(edasi);

//delay(2000);



}
