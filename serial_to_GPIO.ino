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

    // Check if the strings starts with "on" (meaning enable that pin) or "of" (meaning disable that pin)
    if (incoming.substring(0, 2) == "on") {
      // Get the number that they sent alongside the command ("on XX")
      int pin = incoming.substring(3, 5).toInt();
      
      // Check to make sure the pin number works, and enable it if it does, then print that number back out
      if (pin < 1 || pin > 13) {
        Serial.println("error: pin# out of range (should be 1-13)");
      } else {
        digitalWrite(pin, HIGH);
        Serial.print("enabled pin ");
        Serial.println(pin);
        
      }
    } else if (incoming.substring(0, 2) == "of") {
      // Get the number that they sent alongside the command ("of XX")
      int pin = incoming.substring(3, 5).toInt();
      
      // Check to make sure the pin number works, and enable it if it does, then print that number back outs
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
