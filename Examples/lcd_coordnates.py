#!/usr/bin/env python3

'''
#------------------------------------------------------------------------
#
# This is a python Example code for GPS RTK HAT
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

# Example 1
# Display coordinates in lcd display

import serial
import spidev as SPI
from lib import lcdLib_1inch14
from PIL import Image,ImageDraw,ImageFont

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

from lib import ublox_zed_f9p

ser = serial.Serial('/dev/serial0', baudrate=38400, timeout=1)
gps = ublox_zed_f9p.Ublox_F9P(ser)


Font1 = ImageFont.truetype("Font/Arial_Black_Regular.ttf",15)
Font2 = ImageFont.truetype("Font/Arial_Black_Regular.ttf",25)
Font3 = ImageFont.truetype("Font/Font02.ttf",25)
    

disp = lcdLib_1inch14.lcd()
disp.Init()
image2 = Image.new("RGB", (disp.width, disp.height), "WHITE")

image = Image.open('pic/img.jpg')	
disp.Display_image(image)



time.sleep(2)
disp.clear()
draw = ImageDraw.Draw(image2)

draw.text((10,5),"GPS LOCATION", font = Font2, fill = "BLUE")
draw.text((10,50),"Long  = ", font = Font1, fill = "RED")
draw.text((10,80),"Lati  = ", font = Font1, fill = "RED")
disp.Display_image(image2)


try:
    while True:
      try:
            geo = gps.coordinates()
            print("Longitude: ", geo.lon) 
            print("Latitude: ", geo.lat)
            draw.text((80,50),str(round(geo.lon,2)), font = Font1, fill = "RED")
            draw.text((80,80),str(round(geo.lat,2)), font = Font1, fill = "RED")
            disp.Display_image(image2)
      except (ValueError, IOError) as error:
                print(error)

finally:
      ser.close()


