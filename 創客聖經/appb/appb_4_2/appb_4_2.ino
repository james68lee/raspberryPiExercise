void setup() {
    pinMode(13, OUTPUT);
    pinMode(7, INPUT);
    digitalWrite(13, LOW);
}

void loop() {
    int btn_state = digitalRead(7);
    if (btn_state == HIGH) {
        digitalWrite(13, HIGH);
        delay(200);
    } else {
        digitalWrite(13, LOW);
    }
} 