void setup() {
    pinMode(5, OUTPUT);
}

void loop() {
    float pattern[] = {0.8, 0.2, 0.5, 0.6};
    bool flag = true;

    for (int i = 0; i < 20; i++) {
        for (int j = 0; j < 4; j++) {
          if (flag) {
              digitalWrite(5, HIGH);
              flag = false;
          } else {
              digitalWrite(5, LOW);
              flag = true;
          }
          delay(pattern[j] * 1000);
      }
    }
    digitalWrite(5, LOW);
}


