int echo_pin = 2;
int trig_pin = 3;
int delay_us = 10;
long distance_mm = 0;
long duration_us;

const long interval = 250;   
unsigned long previousMillis = 0;

#include <Wire.h>
#include <LIS3MDL.h>
#include <LPS.h>
#include <LSM6.h>
LIS3MDL mag;
LPS ps;
LSM6 imu;
char report[80];
int valguses = 700;

String valgus = "sunlight";
#include <SoftwareSerial.h>
SoftwareSerial mySerial(0, 1);
void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  mySerial.begin(115200);
  Wire.begin();
  pinMode(echo_pin, INPUT);
  
  pinMode(trig_pin, OUTPUT);
  
  if (!ps.init())
  {
    Serial.println("Failed to autodetect pressure sensor!");
    while (1);
  }

  ps.enableDefault();

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
  int sensorvalue = analogRead(A5);

  float pressure = ps.readPressureMillibars();
 
  float temperature = ps.readTemperatureC();
  
  
  previousMillis = currentMillis;
  digitalWrite(trig_pin, HIGH);
  delayMicroseconds(delay_us);
  digitalWrite(trig_pin, LOW);
  delayMicroseconds(delay_us);
  duration_us = pulseIn(echo_pin, HIGH);
  distance_mm = (duration_us/58.0)*10;
  Serial.print(distance_mm);
  Serial.print(" ");
  Serial.print(sensorvalue);
  Serial.print(" ");
  Serial.print(temperature);
  Serial.print(" ");
  Serial.println(pressure);
  }
 // delay(5000);
  //mySerial.write(t);
  //delay(5000);
}
