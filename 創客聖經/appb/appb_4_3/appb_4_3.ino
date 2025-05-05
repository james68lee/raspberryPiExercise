void setup() {
    pinMode(11, OUTPUT);
}

void loop() {
    int duty;
    Serial.begin(9600);
    while (true) {
        if (Serial.available() > 0) {
            duty = Serial.parseInt();
            Serial.println(duty);
            if (duty >= 0 && duty <= 100) {
                analogWrite(11, map(duty, 0, 100, 0, 255));
            }
        }
    }
}

