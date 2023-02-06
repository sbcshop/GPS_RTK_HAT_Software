#!/usr/bin/env python3
# Example 4
# This example sets up the serial port.The function stream_nmea() returns the full NMEA sentence

import serial
from lib import ublox_zed_f9p

ser = serial.Serial('/dev/ttyS0', baudrate=38400, timeout=1)
gps = ublox_zed_f9p.Ublox_F9P(ser)

try:
    while True:
        
        try:
            print(gps.NMEA_Stream())
        except (ValueError, IOError) as error:
            print(error)

finally:
    ser.close()



