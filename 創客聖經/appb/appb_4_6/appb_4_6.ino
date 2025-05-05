void setup() {
    pinMode(11, OUTPUT);
    Serial.begin(9600);
}

void loop() {
    int sensorValue = analogRead(A1);
    float voltage = sensorValue / 1023.0;
    Serial.print("value = ");
    Serial.println(voltage);

    if (voltage > 0.65) {
        digitalWrite(11, LOW);
    } else {
        digitalWrite(11, HIGH);
    }
    delay(500);
}
