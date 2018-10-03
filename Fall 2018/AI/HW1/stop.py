import time
from basicBot import BasicBot
import ev3dev.ev3 as ev3

# set up robot and button response
bttn = ev3.Button()
myRobot = BasicBot("Naruto")

# stop the motors if they are running
myRobot.stop()

# wait for user to press a key
while not bttn.any():
    print(".")
    time.sleep(0.3)   # waits for 0.3 sec before cycling again
