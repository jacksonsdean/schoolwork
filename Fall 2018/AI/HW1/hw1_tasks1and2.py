#!/usr/bin/env python3
import time

from basicBot import BasicBot
import ev3dev.ev3 as ev3

DIST_LIMIT = 50
DIST_MAX = 100

MAX_SPEED = 1

# Set up bot and button response
bttn = ev3.Button()


def read_left_and_right(bot):
    """Turns to the left and right and returns the tuple of the distance from the ultraviolet sensor
    to the left and right of the robot bot"""
    bot.turnLeft(0.2, 0.2)
    left_val = bot.readUltra()
    bot.turnRight(0.2, 0.4)
    right_val = bot.readUltra()
    bot.turnLeft(0.2, 0.2)
    return left_val, right_val


def convert_dist_to_speed(dist):
    """Takes in a distance, forces it between 0 and DIST_MAX and normalizes it from -1 to 1"""
    if dist > DIST_MAX:
        dist = DIST_MAX
    speed = (dist - DIST_LIMIT)/(DIST_MAX - DIST_LIMIT)
    return speed


def one(bot):
    """Tells the bot to move at a speed relative to it's distance from an obstacle. The closer it is to DIST_MAX, the
    slower it goes, if it is closer than DIST_MAX, it moves backwards."""
    while True:
        try:
            dist = bot.readUltra()
            speed = convert_dist_to_speed(dist)
            bot.forward(speed)
            if bttn.any():
                break

        except KeyboardInterrupt:
            break
    bot.stop()


def two_a(bot):
    """Detects distance right and left and then converts these distances to speeds. The left speed is sent to the
    left motor and the right speed is sent to the right motor (ipsalateral)"""
    while True:
        try:
            left_and_right = read_left_and_right(bot)
            left_val = left_and_right[0]
            right_val = left_and_right[1]
            bot.curve(convert_dist_to_speed(left_val), convert_dist_to_speed(right_val))
            time.sleep(1)
            if bttn.any():
                break

        except KeyboardInterrupt:
            break

    bot.stop()


def two_b(bot):
    """Detects distance right and left and then converts these distances to speeds. The right speed is sent to the
    left motor and the left speed is sent to the right motor (contralateral)"""
    while True:
        try:
            left_and_right = read_left_and_right(bot)
            left_val = left_and_right[0]
            right_val = left_and_right[1]
            bot.curve(convert_dist_to_speed(right_val), convert_dist_to_speed(left_val))
            time.sleep(1)
            if bttn.any():
                break

        except KeyboardInterrupt:
            break

    bot.stop()


def line_follow(bot):
    """checks the color sensor of the robot, if the sensor reads white, the robot curves to the left,
    if black then the robot curves to the right, if blue, the robot stops"""
    last_color = 6
    speed = float(input("speed (default .1): "))
    mod = float(input("turn_mod: (default 3): "))
    ev3.Sound.set_volume(100)

    # We need sound! play I walk the line by Johnny Cash
    ev3.Sound.play("line.wav")

    while True:
        try:
            col = bot.readColor()
            left_mod = 1
            right_mod = 1
            ev3.Leds.all_off()
            # white
            if col == 6:
                if last_color != col:
                    # bot.turnRight(0.2, 0.2)
                    # time.sleep(.2)
                    last_color = col
                left_mod = mod
                right_mod = -.5
                ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.AMBER)
                print("white")
            # black
            elif col == 1:
                if last_color != col:
                    # bot.turnLeft(0.2, 0.2)
                    # time.sleep(.2)
                    last_color = col
                right_mod = mod
                left_mod = -.5

                ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.AMBER)
                print("black")
            elif col == 2:
                print("blue - STOP")
                break

            bot.curve(speed * left_mod, speed * right_mod)

            if bttn.backspace:
                break
        except KeyboardInterrupt:
            break

    bot.stop()

if __name__ == '__main__':
    naruto = BasicBot("Naruto")
    naruto.setUltrasonicSensor('in4')
    naruto.setColorSensor('in3')

    choice = ""

    # A menu to select which robot program to run:
    while choice == "":
        choice = input("1. Robot One\n2. Robot 2A\n3. Robot 2B\n4. Follow line\nChoice (1-4): ").lower()
        if "1" in choice:
            one(naruto) # Braitenberg robot 1
        elif "2" in choice:
            two_a(naruto) # Braitenberg robot 2A
        elif"3" in choice:
            two_b(naruto) # Braitenberg robot 2B
        elif "4" in choice:
            line_follow(naruto) # task 2 line following
        else:
            break

    ev3.Leds.all_off()
    # stop the motors if they are running
    naruto.stop()

