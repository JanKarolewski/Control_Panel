#!/usr/bin/python
import time
import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)
door_pin = 2
gpio.setup(door_pin, gpio.IN, pull_up_down=gpio.PUD_UP)  # activate input with Pull-Up

while True:
    if gpio.input(door_pin):
        print("1 - Otwarte")
    else:
        print("0 - Zamkniete")
    time.sleep(0.3)