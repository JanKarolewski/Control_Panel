import time
import RPi.GPIO as gpio

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
gpio.setmode(gpio.BCM)
door_pin = 2
gpio.setup(door_pin, gpio.IN, pull_up_down=gpio.PUD_UP)  # activate input with Pull-Up


while True:

    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    #Red
    low_red = np.array([161,155,84])
    high_red = np.array([179,255,255])
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    red = cv2.bitwise_and(frame, frame, mask = red_mask)
    #cv2.imshow("Frame",frame)
    #cv2.imshow("Red", red)
    key = cv2.waitKey(1)

    if key == 27:
        break

    if (gpio.input(door_pin) and (red_mask = cv2.inRange(hsv_frame, low_red, high_red))):
        print("Wychodzisz z domu, gdy jest włączony piekarnik")
    else:
        print("Wyjscie z domu bezpieczne")
    time.sleep(0.3)