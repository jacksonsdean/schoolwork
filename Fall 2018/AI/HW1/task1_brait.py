#!/usr/bin/env python3
import time

from basicBot import BasicBot
import ev3dev.ev3 as ev3

DIST_LIMIT = 50
DIST_MAX = 100

MAX_SPEED = 1

# set up bot and button response
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
    speed = .5
    while True:
        try:
            col = bot.readColor()
            left_mod = 1
            right_mod = 1
            ev3.Leds.all_off()
            if col == 6:
                # bot.turnLeft(0.2, 0.2)
                left_mod = 1.5

                ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.AMBER)

            elif col == 1:
                # bot.turnRight(0.2, 0.2)
                right_mod = 1.5
                ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.AMBER)
            elif col == 2:
                break

            bot.curve(speed * left_mod, speed * right_mod)

            time.sleep(.1)
            if bttn.backspace:
                break
        except KeyboardInterrupt:
            break

    bot.stop()

if __name__ == '__main__':
    naruto = BasicBot("Naruto")
    naruto.setUltrasonicSensor('in4')
    naruto.setColorSensor('in1')

    while True:
        choice = input("1. Robot One\n2. Robot 2A\n3. Robot 2B\n4. Follow line").lowercase()
        if choice.contains("1"):
            one(naruto)
            break
        elif choice.contains("2"):
            two_a(naruto)
            break
        elif choice.contains("3"):
            two_b(naruto)
            break
        elif choice.contains("4"):
            line_follow(naruto)
            break

    # stop the motors if they are running
    naruto.stop()

