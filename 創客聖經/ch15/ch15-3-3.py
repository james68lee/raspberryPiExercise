from flask import Flask, render_template
from gpiozero import Motor

app = Flask(__name__)

in1 = 18
in2 = 23
in3 = 24
in4 = 25

motor1 = Motor(forward=in1, backward=in2)
motor2 = Motor(forward=in3, backward=in4)
  
@app.route("/")
@app.route("/<cmd>")
def main(cmd=None):
    status = "None..."
    # Forward    
    if cmd == 'f':
        status = "Forward..."
        motor1.forward()
        motor2.forward()
    # Backward    
    if cmd == 'b':
        status = "Backward..."
        motor1.backward()
        motor2.backward()
    # Turn Right   
    if cmd == 'r':
        status = "Turn Right..."
        motor1.forward()
        motor2.stop()
    # Trun Left    
    if cmd == 'l':
        status = "Turn Left..."
        motor1.stop()  
        motor2.forward()      
    # Stop    
    if cmd == 's':
        status = "Stop..."        
        motor1.stop()
        motor2.stop()
    templateData = {
        'title': 'Motor Control',
        'status' : status
    }
    return render_template('motor.html', **templateData)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
