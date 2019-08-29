# Warehouse_Robot_CU

<p align="justify">
This code written in python is for the course taught by Prof. Derek Raemon at University of Colorado Boulder MCEN 5115 Mechantronics and Roboics course S18. THe objective of the course was to build an autonomous robot that can self-navigate itself in a scaled-down version of an automated warehouse following the lane (within yellow lines), stoping at points in front of the particular rack and making sure that the robot is able to pick up the pallet from one location and dropping to its required destination while following all the constraints. 

To perform all these functions, our robot had a drive system to let it move around the city, a vision system to recognize QR codes and navigate through the warehouse, and a pallet picking system to pick up pallets and hold them till its drop-off location.


Hardware: 
1) Raspberry Pi for navigation (by getting coordinates from the Pi-cameras via QR code) and 
2) Rpi Camera: vision (QR Code recognition). 
3) Sparkfun ReadBoard : drive & pallet picking functions.

A number of subsystems go into these 2 major systems which are explained in further detail in the [report](https://drive.google.com/file/d/0B3tR0Eo7ORPncmRURDhOMzExdWNqb1hPbVVWOWU2SlVNOE5V/view?usp=sharing). The total allowable team budget is of $200 for this project.

Arena : 
<p align="center">
  <img src= 'https://drive.google.com/uc?export=view&id=10ChTUNpNnWpRgoYoBaxGUyAMxl-Qc6_D' alt'Arena'>
</p>

Bot :
<p align="center">
  <img src='https://drive.google.com/uc?export=view&id=1JUArJdpUNOD_hTlHR7WjIb3nBsJszVZi' alt='Bot'>
</p>


## Algorithm 1: Navigation / QR Code recognition for MASTER Pi

* Scan Assignment QR Code - send to planning algorithm
    * Get the values of dir. array, “turn” (backward), “rack turn” variables
    * Operate the stepper up to desired row: “array of QR code”
    * Send STOP
* While loop
    * Select dir[0] - “fwd”
    * Redboard - Take Action (forward)
* Scan around the QR codes for a particular one
* After detecting the required code, Verify and throw next action to Redboard.
* Start communication with Pallet Pi - Send flag
  * Stop the motors
  * Send “Rack Turn” Variable
  * For “fwd.” direction, start lane follower on Redboard
* If “turn” (backward) variable exists, send to Redboard
* Follow dir. array
  * Get flag from Pallet Pi
  * Get “turn” variable for pallet pick-up
  * Send Flag to Redboard
  * Flag for jerk
    * If left: motor 2 jerk backwards
    * If right: motor 1 jerk backwards
  * Get continuous flags for pallet pi
  * If flag = yes - execute Pallet pick-up code via Redboard
  * Time_sleep()
  * Break
  * Go back to while loop command.


## Algorithm 2: Pallet Pick-up and Drop-off Algorithm for Pallet Pi

* Get Pallet number from Master Pi
* Get flag from master pi when pallet QR code is detected
* Turn the servo according to “Rack turn” variable
* Send feedback to master pi confirming servo turning
* Keep detecting QR code of pallet
* After recognizing pallet QR code, send flag to master Pi
* Turn servo back to original position
* Get flag from master Pi
* Start alignment code
* QR code is detecting
* Bring QR code in center of frame
* Compare frame center with QR code center (x + w/2)
  * If yes
    * Send flag to master Pi that frame is aligned
    * Master Pi starts pallet pick up code.
  * Else
    * Send flag to master Pi to jerk push on opposite side of QR code
    * (X + w/2) – 200
      * If Positive: left side jerk
      * If negative from left : Motor 2 goes back
      * If negative from right : Motor 1 goes back

USING MQTT FOR SUBSCRIBING AND PUBLISHING WITH MOSQUITTO

## Message Queuing Telemetry Transport (MQTT) 
It is an ISO standard publish-subscribe based messaging protocol, designed for connections with remote locations where a footprint of the code is required. There are number of key choices that code designers made for its usage:

* It is simple to use. Provides a solid building block which can be easily integrated into other solutions.

* Publish-subscribe Service, which is useful for most sensor applications and enables devices to come online and publish ‘stuff’ that was predefined.

## SUBSCRIBING WITH MOSQUITTO:

First, the client is subscribed to ‘debug’. The subscribing command is then used in subscriber window.

* The host flag (-h) is the localhost
* The identity flag (-i) is not required normally.
* The topic flag (-t) is the subscription to the topic ‘debug’

## PUBLISHING WITH MOSQUITTO:

After being linked with ‘debug’, it will be published. After using the code to publish the topic, the
client window gives an output with our topic/message.
</p>
