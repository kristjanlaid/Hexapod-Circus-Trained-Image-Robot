#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

# reference pins by GPIO numbers
GPIO.setmode(GPIO.BCM)
# disable warnings
GPIO.setwarnings(False)

# define row and column pin numbers
row_pins = [21, 20, 16, 19, 13, 6, 5]
col_pins = [27, 22, 4, 14, 15]

# set all the pins as outputs and set column pins high, row pins low
GPIO.setup(col_pins, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(row_pins, GPIO.OUT, initial=GPIO.HIGH)

def show_row(row_number, columns, delay):
    GPIO.output(row_pins[row_number - 1], GPIO.LOW)
    # Control a row of the dot matrix display
    for i in columns:
        GPIO.output(col_pins[i-1], GPIO.HIGH)
    time.sleep(delay)
    for i in columns:
        GPIO.output(col_pins[i-1], GPIO.LOW)

    GPIO.output(row_pins[row_number - 1], GPIO.HIGH)
    
listikene = [[5],[4],[3],[2],[1]]
listikene2 = [7,6,5,4,3,2,1]
def lightshow():
    for i in range(1000):
        show_row(2, [1,2], 0.00001)
#     for i in range(3):
#         for i in range (7):
#             for s in range(300):
#                 show_row(listikene2[i], [1,2,3,4,5], 0.00001)
#         for i in range (7):
#             for s in range(300):
#                 show_row(i+1, [1,2,3,4,5], 0.00001)
#         for i in range (5):
#             for s in range(50):
#                 show_row(1, [i+1], 0.00001)
#                 show_row(2, [i+1], 0.00001)
#                 show_row(3, [i+1], 0.00001)
#                 show_row(4, [i+1], 0.00001)
#                 show_row(5, [i+1], 0.00001)
#                 show_row(6, [i+1], 0.00001)
#                 show_row(7, [i+1], 0.00001)
#         for i in range (5):
#             for s in range(50):
#                 show_row(1, listikene[i], 0.00001)
#                 show_row(2, listikene[i], 0.00001)
#                 show_row(3, listikene[i], 0.00001)
#                 show_row(4, listikene[i], 0.00001)
#                 show_row(5, listikene[i], 0.00001)
#                 show_row(6, listikene[i], 0.00001)
#                 show_row(7, listikene[i], 0.00001)
#         for i in range(5):
#             for i in range (50):
#                 show_row(1, [1,2,4,5], 0.00001)
#                 show_row(2, [1,3,5], 0.00001)
#                 show_row(3, [1,2,4,5], 0.00001)
#                 show_row(4, [1,3,5], 0.00001)
#                 show_row(5, [1,2,4,5], 0.00001)
#                 show_row(6, [1,3,5], 0.00001)
#                 show_row(7, [1,2,4,5], 0.00001)
# 
#             for i in range (50):
#                 show_row(1, [1,3,5], 0.00001)
#                 show_row(2, [2,4], 0.00001)
#                 show_row(3, [1,3,5], 0.00001)
#                 show_row(4, [2,4], 0.00001)
#                 show_row(5, [1,3,5], 0.00001)
#                 show_row(6, [2,4], 0.00001)
#                 show_row(7, [1,3,5], 0.00001)
#         for i in range (5):
#             for s in range(50):
#                 show_row(1, [i+1], 0.00001)
#                 show_row(2, [i+1], 0.00001)
#                 show_row(3, [i+1], 0.00001)
#                 show_row(4, [i+1], 0.00001)
#                 show_row(5, [i+1], 0.00001)
#                 show_row(6, [i+1], 0.00001)
#                 show_row(7, [i+1], 0.00001)
#         for i in range (5):
#             for s in range(50):
#                 show_row(1, listikene[i], 0.00001)
#                 show_row(2, listikene[i], 0.00001)
#                 show_row(3, listikene[i], 0.00001)
#                 show_row(4, listikene[i], 0.00001)
#                 show_row(5, listikene[i], 0.00001)
#                 show_row(6, listikene[i], 0.00001)
#                 show_row(7, listikene[i], 0.00001)
#         for i in range (7):
#             for s in range(300):
#                 show_row(i+1, [1,2,3,4,5], 0.00001)
#         for i in range (7):
#             for s in range(300):
#                 show_row(listikene2[i], [1,2,3,4,5], 0.00001)

    # I
#     show_row(1, [3], 0.00001)
#     show_row(2, [3], 0.00001)
#     show_row(3, [3], 0.00001)
#     show_row(4, [3], 0.00001)
#     show_row(5, [3], 0.00001)
#     show_row(6, [3], 0.00001)
#     show_row(7, [3], 0.00001)
# 
#     # G
#     show_row(1, [2,3,4,5], 0.00001)
#     show_row(2, [1], 0.00001)
#     show_row(3, [1], 0.00001)
#     show_row(4, [1,3,4], 0.00001)
#     show_row(5, [1,5], 0.00001)
#     show_row(6, [1,5], 0.00001)
#     show_row(7, [2,3,4,5], 0.00001)
# 
#      # H
#     show_row(1, [1, 5], 0.00001)
#     show_row(2, [1, 5], 0.00001)
#     show_row(3, [1, 5], 0.00001)
#     show_row(4, [1,2,3,4,5], 0.00001)
#     show_row(5, [1, 5], 0.00001)
#     show_row(6, [1, 5], 0.00001)
#     show_row(7, [1, 5], 0.00001)
# 
#     # T
#     show_row(1, [1,2,3,4,5], 0.00001)
#     show_row(2, [1], 0.00001)
#     show_row(3, [1], 0.00001)
#     show_row(4, [1], 0.00001)
#     show_row(5, [1], 0.00001)
#     show_row(6, [1], 0.00001)
#     show_row(7, [1], 0.00001)
#     
#     # S
#     show_row(1, [2,3,4,5], 0.00001)
#     show_row(2, [1], 0.00001)
#     show_row(3, [1], 0.00001)
#     show_row(4, [2,3,4], 0.00001)
#     show_row(5, [5], 0.00001)
#     show_row(6, [5], 0.00001)
#     show_row(7, [1,2,3,4], 0.00001)
# 
#      # H
#     show_row(1, [1, 5], 0.00001)
#     show_row(2, [1, 5], 0.00001)
#     show_row(3, [1, 5], 0.00001)
#     show_row(4, [1,2,3,4,5], 0.00001)
#     show_row(5, [1, 5], 0.00001)
#     show_row(6, [1, 5], 0.00001)
#     show_row(7, [1, 5], 0.00001)
#     
#     # O
#     show_row(1, [1,2,3,4,5], 0.00001)
#     show_row(2, [1,5], 0.00001)
#     show_row(3, [1,5], 0.00001)
#     show_row(4, [1,5], 0.00001)
#     show_row(5, [1,5], 0.00001)
#     show_row(6, [1,5], 0.00001)
#     show_row(7, [1,2,3,4,5], 0.00001)
# 
#     # W
#     show_row(1, [1, 5], 0.00001)
#     show_row(2, [1, 5], 0.00001)
#     show_row(3, [1, 5], 0.00001)
#     show_row(4, [1, 3, 5], 0.00001)
#     show_row(5, [1, 3, 5], 0.00001)
#     show_row(6, [1, 3, 5], 0.00001)
#     show_row(7, [2, 4], 0.00001)
#     



