char s[] = "#2 P500 S750 T5000";
char t[] = "#2 P1000 S750 T5000"; 

//const int leginput = 0
//const int legoutput = 1
#include <SoftwareSerial.h>
SoftwareSerial mySerial(0, 1);
void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  mySerial.begin(115200);
  mySerial.write(s);
//  pinMode(leginput, INPUT)
//  pinMode(legoutput, OUTPUT)

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
 // delay(5000);
  //mySerial.write(t);
  //delay(5000);
}
