# GPS RTK HAT 

This ZED-F9P-based Raspberry Pi GNSS HAT provides centimeter-level accuracy in seconds. It offers features such as: multi-band RTK with quick convergence times, a high update rate, support for moving base RTK mode, simultaneous reception of four GNSS systems, support for augment positioning systems, accurate & quick positioning with minimal drifting, and exceptional anti-spoofing & anti-jamming capabilities.

<img src = "https://github.com/sbcshop/GPS_RTK_HAT_Software/blob/main/images/img1.png"/>

It can pinpoint your location, your direction, and your path to any place on Earth in less than 30 seconds. Hence, the higher the accuracy, the better! Since GPS Real Time Kinematics (RTK) has mastered fine-tuning its GPS modules' accuracy to only millimetres, we had to incorporate it on this board!

High-precision GPS was improved by SB Components' GPS-RTK HAT. It has the most latest ZED-F9P module from u-blox, which provides 10mm of 3-dimensional precision. These boards can create X, Y, and Z locations that are about the width of your fingernail. You read that correctly. A stream of correction data from an RTCM source and a strong antenna are both necessary for high accuracy GPS.

<img src = "https://github.com/sbcshop/GPS_RTK_HAT_Software/blob/main/images/GPS%20RTK%20PIN.png"/>

## Hardware Overview
#### Battery
A small lithium battery can be seen in the little metal disc immediately to the right of the ZED-F9R module, precisely like the breakout board. The key mechanisms inside the IC that enable a speedy reconnection to satellites are powered by this battery rather than the IC itself, as the 3.3V system does. When it has a lock, the battery will allow for a two-second time to first fix, however the time to first repair will be around 26 seconds. This is referred to as a "hot start," and it continues for four hours after the board is turned off. While the board is powered, the battery steadily charges and may run the backup system for more than a year. Let your module sit for a complete charge.


#### LED’s
Just like the breakout board, there are four LEDs on the bottom left of the board. Starting from the left:

* ***PWR:*** The power LED labeled as PWR will illuminate when 3.3V is activated.
* ***PPS:*** pulse-per-second led indicator. When receiving a basic GPS/GNSS location lock, the module starts flashing at 1Hz.
* ***RTK:*** A real-time kinematic led indicator. when the gadget is operating in standard GPS mode, it stays high. blinking starts when the module enters RTK float                mode after receiving RTCM adjustments. When the module switches to RTK fixed mode and starts to output locations with a precision of a cm, it drops.
* ***GF:*** TA led indication for a geofence. U-Center configuration. will change when a geofence is set up, going high or low. When the module leaves a preset                     boundary, it may be used to start alerts and do other actions.



#### USB
To connect the ZED-F9R to u-center software, you can attach a USB Type-C cable to the connector.

## Features
* Horizontal Position Accuracy:
     * 2.5m without RTK
     * 0.010m with RTK
* Enables simultaneous reception of four GNSS constellations (GPS, BeiDou, Galileo, and GLONASS) while being power efficient.
* Max Velocity: 500m/s 
* Max Altitude: 50km
* It receives both L1C/A and L2C bands
* 4 LEDs for displaying the module's status.
* Supports U-Center, a simple method of configuring the module.
* RTK has several bands, quick convergence times, centimeter-level precision, and a high update rate.
* Current: 68mA - 130mA (varies with constellations and tracking state)
## Communication Protocol
* UART 
   * The ZED-F9P has traditional serial pins. The UART(RX/TX) pins are activated by default. Make that the UART/SPI jumper is open on top of the board. 
   * The ZED-F9P has a second serial port UART2(TX2/RX2) that is mostly utilised for RTCM3 correction data. This port's default behaviour is to automatically accept        and interpret incoming RTCM3 strings, enabling the board's RTK mode.
* I2C 
   *  By default, the I2C pins are enabled.
   
## Steps to Setup With Pi:

**Step.1 -** To start working with our GPS RTK HAT with Rasberry pi/Rock pi, you to setup your pi board to boot by uploading lates OS of it.

**Step.2 -** After that, attach the GPS RTK HAT on your Pi board and power it by providing suitable power supply. 

**Step.3 -** Once your Pi is booted, open command line and type the below command to clone this repository:
```
git clone https://github.com/sbcshop/GPS_RTK_HAT_Software.git
```

**Step.4 -** You can execute any of the examples included in this repository after downloading it to your Raspberry Pi board.
* https://github.com/sbcshop/GPS_RTK_HAT_Software/blob/main/Examples/geo_coords.py
* https://github.com/sbcshop/GPS_RTK_HAT_Software/blob/main/Examples/date_time.py
* https://github.com/sbcshop/GPS_RTK_HAT_Software/blob/main/Examples/nmea_stream.py
* https://github.com/sbcshop/GPS_RTK_HAT_Software/blob/main/Examples/lcd_coordnates.py

## Using GPS RTK HAT Via USB:
<img src = "https://github.com/sbcshop/GPS_RTK_HAT_Software/blob/main/images/img2.JPG" />
 
For using this HAT with USB cable you have to install the USB driver and a Software Application of ublox(U Center). For this you can visit the links below,

[**Download USB Driver**](https://deviceinbox.com/drivers/1870-u-blox-gnss-standard-usb-driver.html)

[**Download Software Application**](https://www.u-blox.com/en/product/u-center) and we have also provided it in this repository. After making these setup follow the steps below:

#### To learn how to use U Center application, click here.
[u-center User guide ](https://github.com/sbcshop/GPS_RTK_HAT_Hardware/blob/main/u-center_Userguide.pdf)

**Step.1 -** After intalling the above mentioned software, plugin your GPS RTK HAT to your system via USB Type-C cable and check for the available COM port. As shon in below image

<img src ="https://github.com/sbcshop/GPS_RTK_HAT_Software/blob/main/images/Scr2.png" />
<img src ="https://github.com/sbcshop/GPS_RTK_HAT_Software/blob/main/images/Scr1.png" />

**Step.2 -** Ublox begins to receive data from numerous satellites from different country as soon as you connect to the correct port, as seen in the figure below.
<img src ="https://github.com/sbcshop/GPS_RTK_HAT_Software/blob/main/images/img.JPG" />
<img src ="https://github.com/sbcshop/GPS_RTK_HAT_Software/blob/main/images/img3.JPG" />


### NMEA Protocol

[NMEA Protocol](https://github.com/sbcshop/GPS_RTK_HAT_Hardware/blob/main/NMEA%20Protocol%20Manual.pdf)

### Ublox ZED-F9P Integration Manual

[Integration Manual](https://github.com/sbcshop/GPS_RTK_HAT_Hardware/blob/main/Ublox%20ZED-F9P_Integration_Manual.pdf)


## Documentation
* [ZED-F9P Datasheet](https://github.com/sbcshop/GPS_RTK_HAT_Hardware/blob/main/Documents/ZED-F9P_DataSheet.pdf)
* [GPS RTK HAT Hardware](https://github.com/sbcshop/GPS_RTK_HAT_Hardware)
* [Getting Started with Raspberry Pi](https://www.raspberrypi.com/documentation/computers/getting-started.html)
* [Raspberry Pi Pico Official website](https://www.raspberrypi.com/documentation/microcontrollers/)
* [Raspberry Pi Datasheet](https://www.raspberrypi.com/documentation/computers/compute-module.html)
* [Hardware Design](https://www.raspberrypi.com/documentation/computers/compute-module.html)
* [Raspberry Pi](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html)


## Related Products

* [GPS HAT](https://shop.sb-components.co.uk/products/gps-hat-for-raspberry-pi?_pos=1&_sid=c0a565487&_ss=r)

 ![GPS HAT](https://cdn.shopify.com/s/files/1/1217/2104/products/GPSHATforRaspberryPi_4.png?v=1648553361&width=400)

## Product License

This is ***open source*** product. Kindly check LICENSE.md file for more information.

Please contact support@sb-components.co.uk for technical support.
<p align="center">
  <img width="360" height="100" src="https://cdn.shopify.com/s/files/1/1217/2104/files/Logo_sb_component_3.png?v=1666086771&width=350">
</p>

