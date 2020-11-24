#include <Wire.h>
#include <LIS3MDL.h>
#include <LPS.h>
#include <LSM6.h>
LIS3MDL mag;
LPS ps;
LSM6 imu;
char report[80];
int valguses = 150;

void setup() {

  Serial.begin(9600);
  Wire.begin();


  // ////////////////////////////////////////////////////////////////////////////////////////

  // 6hur6hk algab

  if (!ps.init())
  {
    Serial.println("Failed to autodetect pressure sensor!");
    while (1);
  }

  ps.enableDefault();

  // 6hur6hk l6ppeb

}


// //////////////////////////////////////////////////////////////////////////////////////


void loop() {

    int sensorValue = analogRead(A5);

    if (sensorValue > valguses){
       Serial.print("The sunlight, it burns!");
    }
    else {
      Serial.print("Hello darkness my old friend...");
    }


  Serial.print(sensorValue);
  
  Serial.println();


  Serial.println();


  // 6hur6hk algab

  float pressure = ps.readPressureMillibars();
 
  float temperature = ps.readTemperatureC();


  Serial.print("Temperature: ");
  Serial.print(temperature);
  Serial.println(" deg C");
  Serial.println();
  Serial.print("Pressure: ");
  Serial.print(pressure);
  Serial.print(" mbar");


  delay(100);

  // 6hur6hk l6ppeb

  Serial.println();
  Serial.println();
  Serial.println();

}
