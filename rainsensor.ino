const int rainSensorPin = A3;
const int buzzerPin = 4;
int threshold = 500;

void setup() {
  Serial.begin(9600);
  pinMode(buzzerPin, OUTPUT);
}

void loop() {
  int rainValue = analogRead(rainSensorPin);

  if (rainValue < threshold) {
    digitalWrite(buzzerPin, HIGH);
    Serial.println("RAIN");
  } else {
    digitalWrite(buzzerPin, LOW);
    Serial.println("NO_RAIN");
  }

  delay(1000);
}

