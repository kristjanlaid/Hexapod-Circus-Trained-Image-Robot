#include <Servo.h> 

Servo myservo;

int edasi = 1600;
int tagasi = 1400;

void setup() {
  
  myservo.attach(11);
  
  Serial.begin(9600); 

}

void loop() {
  
 myservo.writeMicroseconds(1600);

 delay(2000);

 myservo.writeMicroseconds(1400);

 delay(2000);


}
