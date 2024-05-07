# Rahkshi

This described a hardware for Rahkshi car developed by [NetBUG](https://github.com/NetBUG).

This is a simple, self-built chassis with HAL based on Raspberry Pi Pico board. It's based on RP2040 controller.

## Schematics

## Car design
The car follows standard foocars design with two DoF (steering + motor) and two controlling cores: a Raspberry Pi-like computer running Linux
and handling image processing, and a HAL device communicating over Serial port (UART over USB) and dealing with
PPM signals from the remote and controlling the actuators (servo and motor ESC).

## RP2040 + microPython
Read
 - https://www.raspberrypi.com/documentation/microcontrollers/micropython.html
 - https://www.circuitstate.com/tutorials/getting-started-with-raspberry-pi-pico-rp2040-microcontroller-board-pinout-schematic-and-programming-tutorial/#Programming

### RP2040 firmware
Look at https://github.com/AlexandreLarribau/Rasp-Pico-PPM-Reader- and https://github.com/AlexandreLarribau/Rasp-Pico-PPM-Reader-/blob/main/PPMV2.py related
