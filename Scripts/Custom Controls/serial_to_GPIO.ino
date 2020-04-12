using namespace std;

String incoming = ""; // for incoming serial data

void setup() {
  Serial.begin(9600); // opens serial port, sets data rate to 9600 bps
  Serial.println("Ready");
  for(int i = 1; i <= 13; i++) {
    pinMode(i, OUTPUT);
  }
}

void loop() {
  // send data only when you receive data:
  if (Serial.available() > 0) {
    // read the incoming byte:
    incoming = Serial.readString();

    if (incoming.substring(0, 2) == "on") {
      int pin = incoming.substring(3, 5).toInt();
      
      if (pin < 1 || pin > 13) {
        Serial.println("error: pin# out of range (should be 1-13)");
      } else {
        digitalWrite(pin, HIGH);
        Serial.print("enabled pin ");
        Serial.println(pin);
        
      }
    } else if (incoming.substring(0, 2) == "of") {
      int pin = incoming.substring(3, 5).toInt();
      
      if (pin < 1 || pin > 13) {
        Serial.println("error: pin# out of range (should be 1-13)");
      } else {
        digitalWrite(pin, LOW);
        Serial.print("disabled pin ");
        Serial.println(pin);
        
      }
    } else {
      Serial.println("error: improper input formatting, should be \"on pin#\" or \"of pin#\", pin# = 1-13");
    }
  }
}
