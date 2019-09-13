# Cars hardware
The electric architecture looks in the following way.

## Chassis

## Interface
This is a module that connects computing core with the controllable chassis modules (steering servo and motor ESC) and R/C receiver. It can be built on a variety of microcontrollers and MCU boards, most of them being supported with Arduino IDE and PlatformIO: Teensy, chipKIT Fubarino. There is an effort to port the code to simpler ATMega32U4-based MCUs (including Arduino Leonardo) and STM32.
https://www.arduino.cc/reference/en/language/functions/external-interrupts/attachinterrupt/

This is a realtime part of the system. It can be technically implemented with interrupts and PWM on Raspberry Pi using Pigpio, but for the sake of stability and supportability is was moved to a separate unit.

## Computing core
There is currently Raspberry Pi used as a computing core. It is advised to use Model 3B or Model 4, as they provide better multicore performance and larger RAM size.
