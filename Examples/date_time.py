'''
#------------------------------------------------------------------------
#
# This is a python Example code for GPS RTK HAT to get date and time by calling its function
# Written by SB Components Ltd 
#
#==================================================================================
# Copyright (c) SB Components Ltd
#
# Permission is hereby granted, free of charge, to any person obtaining a copy 
# of this software and associated documentation files (the "Software"), to deal 
# in the Software without restriction, including without limitation the rights 
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell 
# copies of the Software, and to permit persons to whom the Software is 
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all 
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE 
# SOFTWARE.
#==================================================================================
'''

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


