#!/usr/bin/env python3
# Example 2
# This example, we call geo_coords() and to get longitude and latitude and many more. 

import serial

from lib import ublox_zed_f9p

ser = serial.Serial('/dev/ttyS0', baudrate=38400, timeout=1)
gps = ublox_zed_f9p.Ublox_F9P(ser)


try:
  while True:
        try:
         coordinate = gps.coordinates()
         print("###########################")
         print("Latitude: ", coordinate.lat)
         print("Longitude: ", coordinate.lon) 
         print("height: ", coordinate.height)
         print("Heading of Motion: ", coordinate.head_motion)
         print("Heading of
               Acceleration: ", coordinate.headAcc)
         print("\n")
        except (ValueError, IOError) as error:
                print(error)

finally:
  ser.close()
