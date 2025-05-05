void setup()
{
    Serial.begin(9600);
    Serial.println("Arduino Uno is Ready");    
}

void loop()
{
    if ( Serial.available() > 0 ) {
        int inByte = Serial.read();
        Serial.print("Data Received: ");
        Serial.print(inByte, DEC);
        Serial.print(" - ");
        Serial.print(inByte, HEX);        
        Serial.println(" (HEX)");                 
    }    
}
