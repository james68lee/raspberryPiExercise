from gpiozero import Motor
from time import sleep

in1 = 18
in2 = 23
in3 = 24
in4 = 25

delay = 1

motor1 = Motor(forward=in1, backward=in2, pwm=True)
motor2 = Motor(forward=in3, backward=in4, pwm=True)
   
def stop():
    motor1.stop()
    motor2.stop()
    
def forward(speed=1):
    motor1.forward(speed)
    motor2.forward(speed)

def backward(speed=1):
    motor1.backward(speed)
    motor2.backward(speed) 
    
def turn_right(speed=0.5):
    motor1.forward(speed)   
    motor2.stop()   
    
def turn_left(speed=0.5): 
    motor1.stop()
    motor2.forward(speed)  
   
speed = 50
print("Speed=", speed)
while True:
    cmd = input("Enter command('q' to exit, speed= 0~100):")
    if cmd.isnumeric():
        speed = int(cmd)
        print("Speed=", speed)
    # Quit
    if cmd == 'q':
        print("Quit")
        motor1.close()
        motor2.close()
        break
    # Forward    
    if cmd == 'go' or cmd == 'g' or cmd == 'f':
        print("Forward...", speed)
        forward(speed/100)
        sleep(delay)
        stop()
    # Backward    
    if cmd == 'back' or cmd == 'b':
        print("Backward...", speed)
        backward(speed/100)
        sleep(delay)
        stop()
    # Turn Right   
    if cmd == 'right' or cmd == 'r':
        print("Turn Right...", speed)
        turn_right(speed/100)
        sleep(delay)
        stop()
    # Trun Left    
    if cmd == 'left' or cmd == 'l':
        print("Turn Left...", speed)
        turn_left(speed/100)
        sleep(delay)
        stop()
    # Stop    
    if cmd == 'stop' or cmd == 's':
        print("Stop...")
        stop()
        
