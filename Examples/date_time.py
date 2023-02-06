#!/usr/bin/env python3
# Example 3
#From here we call dateTime() and to get gps time.

import serial

from lib import ublox_zed_f9p

ser = serial.Serial('/dev/ttyS0', baudrate=38400, timeout=1)
gps = ublox_zed_f9p.Ublox_F9P(ser)


try:
    while True:
        try:
            gps_time = gps.DateTime()
            print("{}/{}/{}".format(gps_time.day, gps_time.month,gps_time.year))
            print("UTC Time {}:{}:{}".format(gps_time.hour, gps_time.min,gps_time.sec))
            #print("Valid date:{}\nValid Time:{}".format(gps_time.valid.validDate, gps_time.valid.validTime))
        except (ValueError, IOError) as error:
            print(error)

finally:
        ser.close()


