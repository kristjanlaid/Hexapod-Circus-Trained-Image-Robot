#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import serial
import json
import signal
import sys
import time

import LCD_display as laul

import Dot_matriks as maatriks

#SERVOBEGIN
import RPi.GPIO as GPIO
from time import sleep

# GPIO.setmode(GPIO.BOARD)
GPIO.setup(17, GPIO.OUT)

pwm = GPIO.PWM(17, 50)

def waveflag():
    pwm.start(0)
    pwm.ChangeDutyCycle(5)
    sleep(2.5)
    pwm.ChangeDutyCycle(7.5)
    sleep(2.5)
    pwm.stop()
#     GPIO.cleanup()
#SERVOEND

#IMAGEDETECTIONBEGIN
import cv2
import numpy as np
#camera img
cap = cv2.VideoCapture(0)


template1 = cv2.imread('Dorito.png',0)

template2 = cv2.imread('just_a_star.png',0)

template3 = cv2.imread('love.png',0)

template4 = cv2.imread('pi.png',0)

template5 = cv2.imread('square.png',0)

template6 = cv2.imread('stonks.png',0)

template7 = cv2.imread('treasure.png',0)

def exists(frame, template, thresh, original):
        a = True
        res = cv2.matchTemplate(frame, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= thresh)
        w, h = template.shape[::-1]

        
        if len(loc[-1]) == 0:
            a = False
            

        for pt in zip(*loc[::-1]):
            if res[pt[1]][pt[0]] == 1:
                a = False

        if a != False:
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
            top_left = max_loc
            bottom_right = (top_left[0] + w, top_left[1] + h)
#             cv2.rectangle(frame,top_left, bottom_right, 255, 2)
            cv2.rectangle(original,top_left, bottom_right, 255, 2)
            return True
#IMAGEDETECTIONEND
def initialize_serial(com_port, baudrate=115200):
    """
    This function creates serial object and checks if the data is sent by request
    """
    try:
        ser = serial.Serial(com_port, baudrate=baudrate, timeout=2)
        return True, ser

    except (serial.SerialException or ValueError) as e:
        print("Failed to establish a serial connection: " + str(e))
        return False, None


def send_data(ser, kask):

    try:
        # Request data
        ser.write(kask.encode())

        # Wait for a response to reach us from Arduino for two seconds,
        # if a response arrives convert it to a dictionary
    except:
        print("erorsend")
def read_data(ser):
    try:
#         ser.write("R".encode())
        ser.flushInput()
        a = ser.readline().decode().strip()
    except:
        print("erorread")
    finally:
        return a
        


def close(message=""):
    global running, ser
    running = False
    if ser.is_open:
        ser.close()
    print(message)
    sys.exit(0)


def signal_handler(sig, frame):
    """
    This function will be called when CTRL+C is pressed
    """
    close('\nYou pressed Ctrl+C! Closing the program nicely :)')

pildiotsimine = 1
pilt1tegevus = 0
pilt2tegevus = 0
pilt3tegevus = 0
pilt4tegevus = 0
pilt5tegevus = 0
pilt6tegevus = 0
pilt7tegevus = 0
if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)

    running, ser = initialize_serial('/dev/ttyUSB0')
#     send_data(ser, "#0 P1100 #4 P1100 #8 P1100 #16 P1000 #20 P1100 #24 P1100 T1000\n\r")
#     send_data(ser, "#5 P1900 #9 P1200 T3000\n\r")
#     send_data(ser, "#1 P1200 #5 P1200 #9 P700 #17 P1200 #21 P1100 #25 P1200 T3000\n\r")

#     send_data(ser, "#2 P1100 T3000\n\r")
    time.sleep(0.2)
    send_data(ser, "#1 P1300 #5 P1300 #9 P650 #17 P1700 #21 P1600 #25 P1700 T3000\n\r") #keskel seishoiak
    time.sleep(0.2)
    send_data(ser, "#2 P1100 #6 P1100 #10 P1100 #18 P1900 #22 P1900 #26 P1900 T3000\n\r")
    time.sleep(0.2)
    send_data(ser, "#8 P1500 #24 P1500 #16 P1400 #20 P1500 #0 P1500 #4 P1500 T3000\n\r")
    time.sleep(5)
    #kondimine
    send_data(ser, "#1 P1700 #9 P1050 #21 P1200 T1500\n\r")
    time.sleep(1.6)
    send_data(ser, "#5 P1100 #24 P1200 #16 P1700 #4 P1300 T1500\n\r")
    send_data(ser, "#8 P1800 #20 P1300 #0 P1200 T1500\n\r")
    time.sleep(1.6)
    send_data(ser, "#1 P1300 #9 P650 #21 P1600 T1500\n\r")
    time.sleep(1.6)
    send_data(ser, "#17 P1500 #25 P1400 #5 P1900 T1500\n\r")
    time.sleep(1.6)
    send_data(ser, "#5 P1300 #8 P1500 #20 P1500 #0 P1500 T1500\n\r")
    send_data(ser, "#24 P1500 #16 P1400 #4 P1500 T1500\n\r")
    time.sleep(1.6)
    send_data(ser, "#17 P1700 #25 P1700 #5 P1300 T1500\n\r")

    
#     #tantsuliigutus 5 ja 21
#     send_data(ser, "#5 P1900 #21 P1000 T500\n\r")
#     time.sleep(0.6)
#     send_data(ser, "#22 P1100 #6 P1900 T250\n\r")
#     time.sleep(0.3)
#     send_data(ser, "#22 P1900 #6 P1100 T250\n\r")
#     time.sleep(0.3)
#     send_data(ser, "#5 P1300 #21 P1600 T500\n\r")
#     time.sleep(0.6)
#     #ulesalla
#     send_data(ser, "#1 P1600 #5 P1600 #9 P950 #17 P1400 #21 P1300 #25 P1400 T500\n\r")
#     send_data(ser, "#2 P1400 #6 P1400 #10 P1400 #18 P1600 #22 P1600 #26 P1600 T500\n\r")
#     time.sleep(0.6)
#     send_data(ser, "#1 P1300 #5 P1300 #9 P650 #17 P1700 #21 P1600 #25 P1700 T500\n\r")
#     send_data(ser, "#2 P1100 #6 P1100 #10 P1100 #18 P1900 #22 P1900 #26 P1900 T500\n\r")
#     time.sleep(0.6)
#     #tantsuliigutus 25 ja 1
#     send_data(ser, "#25 P1100 #1 P1900 T500\n\r")
#     time.sleep(0.6)
#     send_data(ser, "#26 P1100 #2 P1900 T250\n\r")
#     time.sleep(0.3)
#     send_data(ser, "#26 P1900 #2 P1100 T250\n\r")
#     time.sleep(0.3)
#     send_data(ser, "#25 P1700 #1 P1300 T500\n\r")
#     time.sleep(0.6)
#     #ulesalla
#     send_data(ser, "#1 P1600 #5 P1600 #9 P950 #17 P1400 #21 P1300 #25 P1400 T500\n\r")
#     send_data(ser, "#2 P1400 #6 P1400 #10 P1400 #18 P1600 #22 P1600 #26 P1600 T500\n\r")
#     time.sleep(0.6)
#     send_data(ser, "#1 P1300 #5 P1300 #9 P650 #17 P1700 #21 P1600 #25 P1700 T500\n\r")
#     send_data(ser, "#2 P1100 #6 P1100 #10 P1100 #18 P1900 #22 P1900 #26 P1900 T500\n\r")
#     time.sleep(0.6)
#     #tantsuliigutus 9 ja 17
#     send_data(ser, "#9 P1500 #17 P1100 T500\n\r")
#     time.sleep(0.6)
#     send_data(ser, "#10 P1900 #18 P1100 T250\n\r")
#     time.sleep(0.3)
#     send_data(ser, "#10 P1100 #18 P1900 T250\n\r")
#     time.sleep(0.3)
#     send_data(ser, "#9 P650 #17 P1700 T500\n\r")
#     time.sleep(0.6)
#     #ulesalla
#     send_data(ser, "#1 P1600 #5 P1600 #9 P950 #17 P1400 #21 P1300 #25 P1400 T500\n\r")
#     send_data(ser, "#2 P1400 #6 P1400 #10 P1400 #18 P1600 #22 P1600 #26 P1600 T500\n\r")
#     time.sleep(0.6)
#     send_data(ser, "#1 P1300 #5 P1300 #9 P650 #17 P1700 #21 P1600 #25 P1700 T500\n\r")
#     send_data(ser, "#2 P1100 #6 P1100 #10 P1100 #18 P1900 #22 P1900 #26 P1900 T500\n\r")
#     time.sleep(0.6)
    
#     time.sleep(3.5)

#     send_data(ser, "#2 P1900 #6 P1900 #10 P1900 #18 P1100 #22 P1100 #26 P1100 T2000\n\r")
#     time.sleep(2.5)
#     send_data(ser, "#2 P1500 #6 P1500 #10 P1500 #18 P1500 #22 P1500 #26 P1500 T2000\n\r")
#     time.sleep(2.5)
#     send_data(ser, "#1 P1500 #5 P1500 #9 P850 #17 P1500 #21 P1400 #25 P1500 #2 P1500 #6 P1500 #10 P1500 #18 P1500 #22 P1500 #26 P1500 T3000\n\r")
#     time.sleep(3.5)
#     send_data(ser, "#17 P1300 T1000\n\r")
    while running:
#         while pildiotsimine == 1:
#             ret, frame = cap.read()
# 
#             grayboy = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# 
#             if exists(grayboy, template1, 0.5, frame) == True:
#                 print("Tasty dorito")
#                 pilt1tegevus = 1
#                 pildiotsimine = 0
#             elif exists(grayboy, template2, 0.35, frame) == True:
#                 print("Milky way")
#                 pilt2tegevus = 1
#                 pildiotsimine = 0
#             elif exists(grayboy, template3, 0.3, frame) == True:
#                 print("Very sweet")
#                 pilt3tegevus = 1
#                 pildiotsimine = 0
#             elif exists(grayboy, template4, 0.4, frame) == True:
#                 print("Looks quite round")
#                 pilt4tegevus = 1
#                 pildiotsimine = 0
#             elif exists(grayboy, template5, 0.5, frame) == True:
#                 print("Lego?")
#                 pilt5tegevus = 1
#                 pildiotsimine = 0
#             elif exists(grayboy, template6, 0.4, frame) == True:
#                 print("Stonk market")
#                 pilt6tegevus = 1
#                 pildiotsimine = 0
#             elif exists(grayboy, template7, 0.5, frame) == True:
#                 print("Captain Jack Sparrow is calling")
#                 pilt7tegevus = 1
#                 pildiotsimine = 0
#             cv2.imshow('Original with detection', frame)
#             if cv2.waitKey(1) & 0xFF == ord('q'):
#                 break
#         waveflag()
#         laul.Ijustmetyou()
#         while pildiotsimine == 0:
#             if pilt1tegevus == 1:
#                 waveflag()
#                 pilt1tegevus = 0
#                 pildiotsimine = 1
#             elif pilt2tegevus == 1:
#                 print(read_data(ser))
#                 pilt2tegevus = 0
#                 pildiotsimine = 1
#             elif pilt3tegevus == 1:
#                 laul.Ijustmetyou()
#                 pilt3tegevus = 0
#                 pildiotsimine = 1
#             elif pilt4tegevus == 1:
# #                 maatriks.lightshow()
#                 pilt4tegevus = 0
#                 pildiotsimine = 1
#             elif pilt5tegevus == 1:
#                 waveflag()
#                 pilt5tegevus = 0
#                 pildiotsimine = 1
#             elif pilt6tegevus == 1:
#                 waveflag()
#                 pilt6tegevus = 0
#                 pildiotsimine = 1
#             elif pilt7tegevus == 1:
#                 waveflag()
#                 pilt7tegevus = 0
#                 pildiotsimine = 1
#         print(read_data(ser))
#         
#         send_data(ser, "#17 P1500 T500\n\r")
#         time.sleep(0.6)
#         send_data(ser, "#17 P1300 T500\n\r")
#         time.sleep(0.6)
#         waveflag()

#         time.sleep(5)
#         send_data(ser, "#2 P800 #6 P800 #10 P800 #18 P2100 #22 P2100 #26 P2100 T2000\n\r")
#         time.sleep(2.5)
#         send_data(ser, "#2 P2100 #6 P2100 #10 P2100 #18 P800 #22 P800 #26 P800 T2000\n\r")
#         time.sleep(2.5)
#         send_data(ser, "#6 P600 S750 T500\n\r")
#         send_data(ser, "#10 P600 S750 T500\n\r")
#         send_data(ser, "#18 P2400 S750 T500\n\r")
#         send_data(ser, "#22 P2400 S750 T500\n\r")
#         send_data(ser, "#26 P2400 S750 T500\n\r")
#         time.sleep(5)
#         send_data(ser, "#2 P2200 S750 T500\n\r")
#         send_data(ser, "#6 P2200 S750 T500\n\r")
#         send_data(ser, "#10 P2200 S750 T500\n\r")
#         send_data(ser, "#18 P800 S750 T500\n\r")
#         send_data(ser, "#22 P800 S750 T500\n\r")
#         send_data(ser, "#26 P800 S750 T500\n\r")

        if not ser.is_open:
            close("Serial is closed!")

        # Throttle the loop to about 10 times per second
cv2.waitKey(0)
cv2.destroyAllWindows()