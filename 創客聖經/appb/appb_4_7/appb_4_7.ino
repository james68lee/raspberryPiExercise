#include <Servo.h>

Servo servo3;
int pre_pos = 0;

void setup() {
    servo3.attach(3);
    Serial.begin(9600);
}

void loop() {
    int sensorValue = analogRead(A0);
    float voltage = sensorValue / 1023.0;
    int curr_pos = int(voltage * 179);

    if (curr_pos != pre_pos) {
        Serial.print("Angle = ");
        Serial.println(curr_pos);
        servo3.write(curr_pos);
        pre_pos = curr_pos;
    }
}