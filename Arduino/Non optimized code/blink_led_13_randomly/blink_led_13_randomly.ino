boolean state; // State of the LED.
int maxDelay; // Max delay after a tick.
int ledId; // LED id.

void setup() {
  state = false;
  maxDelay = 1000;
  ledId = 13;
  pinMode(ledId, OUTPUT); // LED 13 is now in OUTPUT mode.
}

void loop() {
  state = !state; // state is now its contrary.
  digitalWrite(ledId, state);
  delay(random(maxDelay));
}
