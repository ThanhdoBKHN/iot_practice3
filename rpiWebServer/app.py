# import RPi.GPIO as GPIO 
from flask import Flask, render_template, request 
app = Flask(__name__) 
#GPIO.setmode(GPIO.BCM) 
#GPIO.setwarnings(False) 
ledRed = 13 
ledYellow= 19 
ledGreen= 26 
ledRedSts = 0
ledYellowSts = 0 
ledGreenSts = 0 
#GPIO.setup(ledRed, GPIO.OUT) 
#GPIO.setup(ledYellow,GPIO.OUT) 
#GPIO.setup(ledGreen, GPIO.OUT) 
#GPIO.output(ledRed, GPIO.LOW) 
#GPIO.output(ledYellow, GPIO.LOW) 
#GPIO.output(ledGreen, GPIO.LOW) 
@app.route('/') 
def index(): 
    ledRedSts = str(ledRed) + " OFF" 
    ledYellowSts = str(ledYellow) + " OFF" 
    ledGreenSts = str(ledGreen) + " OFF" 
    templateData = { 'ledRed' : ledRedSts, 'ledYellow' : ledYellowSts, 'ledGreen' : ledGreenSts } 
    return render_template('index.html', **templateData)
@app.route('/<deviceName>/<action>') 
def do(deviceName, action): 
    ledRedS = " OFF"
    ledYellowS = " OFF"
    ledGreenS = " OFF"

    if deviceName == "ledRed" and action == "on": 
        actuator = ledRed 
        ledRedS = " ON"
    if deviceName == "ledYellow" and action == "on": 
        actuator = ledYellow 
        ledYellowS = " ON"
    if deviceName == "ledGreen" and action == "on": 
        actuator = ledGreen 
        ledGreenS = " ON"
    if deviceName == "ledRed" and action == "off": 
        actuator = ledRed 
        ledRedS = " OFF"
    if deviceName == "ledYellow" and action == "off": 
        actuator = ledYellow 
        ledYellowS = " OFF"
    if deviceName == "ledGreen" and action == "off": 
        actuator = ledGreen 
        ledGreenS = " OFF"

    if action == "on": 
        actuator = 1
    if action == "off": 
        actuator = 0

    ledRedSts = str(ledRed) + ledRedS
    ledYellowSts = str(ledYellow) + ledYellowS
    ledGreenSts = str(ledGreen) + ledGreenS
    templateData = { 'ledRed' : ledRedSts, 'ledYellow' : ledYellowSts, 'ledGreen' : ledGreenSts}
    return render_template('index.html', **templateData )

if __name__ == '__main__': 
    app.run(debug=True,host='0.0.0.0')