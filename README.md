# GPS RTK HAT 

With GPS, you can determine your location, your direction, and your route to any location on Earth in less than 30 seconds. Therefore, the better the precision, the higher! We had to include it on this board since GPS Real Time Kinematics (RTK) has perfected fine-tuning the accuracy of their GPS modules to just millimetres!

The GPS-RTK HAT from SB Components set a higher standard for high-precision GPS. It is equipped with the most recent ZED-F9P module from u-blox, which allows for 10mm of 3-dimensional accuracy. These boards can produce your X, Y, and Z location that is around the width of your fingernail. You read that right. High precision GPS necessitates both a stream of correction data from an RTCM source and a good view of the sky (sorry, no indoor site). If you have two ZED-F9P breakout boards or access to an online correction source, your ZED-F9P can output latitude, longitude, and altitude with centimeter-grade accuracy.

## Hardware Overview

Specifications Image(.jpg)


## Battery
Just like the breakout board, the small metal disk just to the right of the ZED-F9R module is a small lithium battery. This battery does not provide power to the IC as the 3.3V system does, but to relevant systems inside the IC that allow for a quick reconnection to satellites. The time to first fix will be about ~26 seconds, but after it has a lock, that battery will allow for a two-second time to first fix. This is known as a hot start and lasts for four hours after the board is powered down. The battery provides over a year's worth of power to the backup system and charges slowly when the board is powered. To charge it to full, leave your module plugged in for 48 hours.


## LED’s
Just like the breakout board, there are four LEDs on the bottom left of the board. Starting from the left:

* ***PWR:*** The power LED labeled as PWR will illuminate when 3.3V is activated.
* ***PPS:*** The pulse per second LED labeled as PPS will illuminate each second once a position lock has been achieved. This generates a pulse that is synchronized with a GPS or UTC time grid. By default, you'll see one pulse a second.

* ***RTK:*** The RTK LED will be illuminated constantly upon power-up. Once RTCM data has been successfully received it will begin to blink. This is a good way to see if the ZED-F9R is getting RTCM from various sources. Once an RTK fix is obtained, the LED will turn off.

* ***GF:*** The GEO LED can be configured to turn on/off for geofencing applications.




## USB
To connect the ZED-F9R to u-center software, you can attach a USB Type-C cable to the connector. Keep in mind that the power pin is not connected to the USB-C connector. You will need to draw power from the qwiic connector or the Pi's 2x20 header pins.





## Documentation

* [GPS RTK HAT Hardware](https://github.com/sbcshop/GPS_RTK_HAT_Hardware)
* [Getting Started with Raspberry Pi](https://www.raspberrypi.com/documentation/computers/getting-started.html)
* [Raspberry Pi Pico Official website](https://www.raspberrypi.com/documentation/microcontrollers/)
* [Raspberry Pi Datasheet](https://www.raspberrypi.com/documentation/computers/compute-module.html)
* [Hardware Design](https://www.raspberrypi.com/documentation/computers/compute-module.html)
* [Raspberry Pi](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html)

## Related Products

* [RFID HAT for RaspberryPi](https://shop.sb-components.co.uk/products/rfid-hat-for-raspberry-pi?_pos=3&_sid=59f725ea2&_ss=r)

 ![RFID HAT for RaspberryPi](https://cdn.shopify.com/s/files/1/1217/2104/products/RFIDforPi.jpg?v=1614587676&width=400)

* [RaspberryPi Pico RFID Expansion](https://shop.sb-components.co.uk/products/raspberry-pi-pico-rfid-expansion?_pos=3&_sid=075681430&_ss=r)

 ![RaspberryPi Pico RFID Expansion](https://cdn.shopify.com/s/files/1/1217/2104/products/2_85a5dfb2-96cb-4e0b-ba28-a70af127a4f1.png?v=1613732653&width=400)
 
* [UHF HAT For Raspberry-Pi](https://shop.sb-components.co.uk/products/uhf-hat-for-raspberry-pi?_pos=1&_sid=4a8407538&_ss=r)

 ![UHF HAT For Rpi](https://cdn.shopify.com/s/files/1/1217/2104/products/UHFHATForRaspberryPi.png?v=1648192425&width=400)
  
## Product License

This is ***open source*** product. Kindly check LICENSE.md file for more information.

Please contact support@sb-components.co.uk for technical support.
<p align="center">
  <img width="360" height="100" src="https://cdn.shopify.com/s/files/1/1217/2104/files/Logo_sb_component_3.png?v=1666086771&width=350">
</p>

