from flask import Flask, render_template
from gpiozero import LED

app = Flask(__name__)

leds = [LED(18), LED(23)]
states = [False, False]

def update_leds():
    for i, value in enumerate(states):
        if value == True:
            leds[i].on()
        else:
            leds[i].off() 
  
@app.route("/")
@app.route("/<led>")
def main(led='-1'):
    if led >= '0' and led <='1':
        pos = int(led)
        states[pos] = not states[pos]
        update_leds()
    templateData = {
        'title': 'GPIO Control',
        'LED0' : str(states[0]), 
        'LED1' : str(states[1])
    }
    return render_template('gpio.html', **templateData)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
