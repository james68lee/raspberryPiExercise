void setup() {
    pinMode(11, OUTPUT);
    Serial.begin(9600);
}

void loop() {
    int sensorValue = analogRead(A0);
    float voltage = sensorValue / 1023.0;
    analogWrite(11, voltage * 255);
    delay(500);
}

