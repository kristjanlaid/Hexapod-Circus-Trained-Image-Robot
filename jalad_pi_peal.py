#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import serial
import json
import signal
import sys
import time


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
    """
    Retrieve data from ultrasonic sensor and line following module connected to Arduino
    """
    try:
        # Request data
        ser.write(kask.encode())

        # Wait for a response to reach us from Arduino for two seconds,
        # if a response arrives convert it to a dictionary
    except:
        print("")



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


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)

    running, ser = initialize_serial('/dev/ttyUSB0')

    send_data(ser, "#1 P1500 S750 T3000\n\r")
    send_data(ser, "#5 P1500 S750 T3000\n\r")
    #servo 9 on valesti kalibreeritud
    send_data(ser, "#9 P850 S750 T3000\n\r")
    send_data(ser, "#17 P1500 S750 T3000\n\r")
    send_data(ser, "#21 P1400 S750 T3000\n\r")
    send_data(ser, "#25 P1500 S750 T3000\n\r")
    while running:
#         time.sleep(5)
#         send_data(ser, "#2 P600 S750 T500\n\r")
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
        time.sleep(1)
