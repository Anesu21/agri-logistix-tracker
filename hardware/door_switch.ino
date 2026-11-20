const int doorSwitchPin = 3;
volatile bool doorOpened = false;

void setup() {
  Serial.begin(9600);
  pinMode(doorSwitchPin, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(doorSwitchPin), doorOpenedISR, FALLING);
}

void loop() {
  if (doorOpened) {
    Serial.println("ALERT: Door OPENED!");
    doorOpened = false; 
  }
  delay(100);
}

void doorOpenedISR() {
  doorOpened = true;
}
