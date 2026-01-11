from flask import Flask, jsonify, render_template
import serial
import time

app = Flask(__name__)

# CHANGE COM PORT IF REQUIRED
arduino = serial.Serial(
    port='COM3',
    baudrate=9600,
    timeout=1,
    exclusive=True
)


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
        print("From Arduino:", data)   # 👈 IMPORTANT

        if data == "RAIN":
            rain_status = "RAIN"
        elif data == "NO_RAIN":
            rain_status = "NO_RAIN"

    return jsonify({"status": rain_status})

if __name__ == "__main__":
    app.run(port=5000)
