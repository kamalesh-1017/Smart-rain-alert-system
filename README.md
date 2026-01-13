🌧 Rain Detection System using Arduino, Python & Web Dashboard

A real-time Rain Detection and Monitoring System built using Arduino UNO, Rain Sensor Module, Python (Flask), and a modern web dashboard UI.
The system detects rain, triggers a buzzer alert, and displays the live status on a web page.

📌 Project Overview

This project reads data from a rain sensor connected to an Arduino.
The Arduino sends rain status (RAIN / NO_RAIN) via serial communication to a Python Flask backend.
The backend serves a web dashboard that updates live using JavaScript.

🧠 System Architecture
Rain Sensor → Arduino UNO → USB Serial
                           ↓
                    Python (Flask)
                           ↓
                   Web Dashboard (UI)

🔧 Hardware Components

Arduino UNO

Rain Sensor Module

Buzzer

USB Cable

Jumper Wires

🔌 Circuit Connections
Component	Arduino Pin
Rain Sensor AO	A3
Rain Sensor VCC	Vin
Rain Sensor GND	GND
Buzzer (+)	Digital Pin 4
Buzzer (−)	GND
🧰 Software Requirements

Arduino IDE

Python 3.10+

Flask

PySerial

Web Browser (Chrome / Edge / Firefox)

📦 Python Libraries

Install required libraries using:

pip install flask pyserial

📁 Project Structure
RainSensor/
│
├── app.py
│
└── templates/
    └── index.html


CSS and JavaScript are embedded directly inside index.html using <style> and <script> tags.

🧪 Arduino Code

Upload the following code to Arduino UNO:

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

🐍 Python Backend (Flask)

app.py

from flask import Flask, jsonify, render_template
import serial
import time

app = Flask(__name__)

arduino = serial.Serial('COM3', 9600, timeout=1)  # Change COM port if needed
time.sleep(2)

rain_status = "WAITING"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rain')
def rain():
    global rain_status

    if arduino.in_waiting > 0:
        data = arduino.readline().decode(errors='ignore').strip()
        if data in ["RAIN", "NO_RAIN"]:
            rain_status = data

    return jsonify({"status": rain_status})

if __name__ == "__main__":
    app.run(port=5000)

🌐 Web Dashboard

Displays RAIN / NO RAIN

Color-coded status

Auto-updates every second

Modern glass-morphism UI

▶️ How to Run the Project
Step 1: Upload Arduino Code

Upload Arduino sketch

Test with Serial Monitor

Close Serial Monitor after testing

Step 2: Run Python Backend (CMD Recommended)
cd C:\Users\mkama\Downloads\RainSensor
python app.py

Step 3: Open Web Dashboard

Open browser and visit:

http://127.0.0.1:5000

⚠️ Important Notes

Only one application can access the COM port at a time

Close Arduino IDE while running Python

Always run Python from CMD, not VS Code Run button

✅ Output
Condition	Web Display	Buzzer
Dry	☀ NO RAIN (Green)	OFF
Wet	🌧 RAIN DETECTED (Red)	ON
🚀 Future Enhancements

IoT cloud integration

Rain intensity graph

Mobile app support

SMS / Email alerts

ESP8266 / ESP32 WiFi support

📚 Use Cases

Smart weather monitoring

Agriculture automation

Smart home rain alert

College mini-project / IoT demo

🧑‍💻 Author

Kamalesh
Electronics & Software Enthusiast

📜 License

This project is open-source and free to use for educational purposes.
