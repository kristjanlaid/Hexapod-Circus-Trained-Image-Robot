

int echo_pin = 2;
int trig_pin = 3;

int delay_us = 10;

long distance_mm = 0;
long duration_us;

void setup()  {

  Serial.begin(9600);
  pinMode(echo_pin, INPUT);
  pinMode(trig_pin, OUTPUT);

}

void loop() {

    digitalWrite(trig_pin, HIGH);
    delayMicroseconds(delay_us);
    digitalWrite(trig_pin, LOW);

    duration_us = pulseIn(echo_pin, HIGH);


    distance_mm = (duration_us / 5.8);

    Serial.println(distance_mm);
    
    delay(1000);
}
