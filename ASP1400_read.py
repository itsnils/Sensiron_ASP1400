# Read the Serial Sensiron ASP1400 Bidirectional Differential Pressure Meter on Raspberry Pi 4B
# https://www.mouser.com/datasheet/2/682/Sensirion_Differential_Pressure_Sensors_ASP1400_Da-1274201.pdf
# Q3 2019 Python 3.7

import os, sys
import serial

"""
reads the serial port and prints the value
"""

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=5)  # select the correct serial device '/dev/ttyUSB0'

while True:
    line = ser.readline()
    if len(line) == 0:
        print("Time out! Exit.\n")
        sys.exit()

    print(line)
