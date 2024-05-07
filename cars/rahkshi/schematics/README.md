# Rahkshi

This described a hardware for Rahkshi car developed by [NetBUG](https://github.com/NetBUG).

This is a simple, self-built chassis with HAL based on Raspberry Pi Pico board. It's based on RP2040 controller.

## Schematics

## Car design
The car follows standard foocars design with two DoF (steering + motor) and two controlling cores: a Raspberry Pi-like computer running Linux
and handling image processing, and a HAL device communicating over Serial port (UART over USB) and dealing with
PPM signals from the remote and controlling the actuators (servo and motor ESC).
