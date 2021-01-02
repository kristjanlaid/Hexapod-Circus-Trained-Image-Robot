int echo_pin = 2;
int trig_pin = 3;
int delay_us = 10;
long distance_mm = 0;
long duration_us;

const long interval = 250;   
unsigned long previousMillis = 0;

#include <SoftwareSerial.h>
SoftwareSerial mySerial(0, 1);
void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  mySerial.begin(115200);
  pinMode(echo_pin, INPUT);
  
  pinMode(trig_pin, OUTPUT);
  


}

void loop() {
  // put your main code here, to run repeatedly:
  //mySerial.write(s);
  while (mySerial.available()){
    Serial.write(mySerial.read());
  }
  while (Serial.available()){
    mySerial.write(Serial.read());
  }
  unsigned long currentMillis = millis();

  if (currentMillis - previousMillis >= interval) {
  previousMillis = currentMillis;
  digitalWrite(trig_pin, HIGH);
  delayMicroseconds(delay_us);
  digitalWrite(trig_pin, LOW);
  delayMicroseconds(delay_us);
  duration_us = pulseIn(echo_pin, HIGH);
  distance_mm = (duration_us/58.0)*10;
  Serial.println(distance_mm);
  }
 // delay(5000);
  //mySerial.write(t);
  //delay(5000);
}
