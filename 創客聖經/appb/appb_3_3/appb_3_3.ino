const int ledPin = 13;
int dTime = 1000;

void setup()
{
    pinMode(ledPin, OUTPUT); 
    Serial.begin(9600);    
}

void loop()
{
    dTime = dTime - 100;
    if ( dTime <= 0 ) {
        dTime = 1000;
    }
    Serial.print("Delay Time = ");
    Serial.println(dTime);    
    digitalWrite(ledPin, HIGH);
    delay(dTime);
    digitalWrite(ledPin, LOW);
    delay(dTime);    
}
