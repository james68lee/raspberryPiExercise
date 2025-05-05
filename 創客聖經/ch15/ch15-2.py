from gpiozero import Motor

in1 = 18
in2 = 23
in3 = 24
in4 = 25

motor1 = Motor(forward=in1, backward=in2)
motor2 = Motor(forward=in3, backward=in4)
   
while True:
    cmd = input("Enter command('q' to exit):")
    # Quit
    if cmd == 'q':
        print("Quit")
        motor1.stop()
        motor2.stop()
        break
    # Forward    
    if cmd == 'go' or cmd == 'g' or cmd == 'f':
        print("Forward...")
        motor1.forward()
        motor2.forward()
    # Backward    
    if cmd == 'back' or cmd == 'b':
        print("Backward...")
        motor1.backward()
        motor2.backward()
    # Turn Right   
    if cmd == 'right' or cmd == 'r':
        print("Turn Right...")
        motor1.forward()
        motor2.stop()
    # Trun Left    
    if cmd == 'left' or cmd == 'l':
        print("Turn Left...")
        motor1.stop()
        motor2.forward()
    # Stop    
    if cmd == 'stop' or cmd == 's':
        print("Stop...")
        motor1.stop()
        motor2.stop()
