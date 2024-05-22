# Rahkshi Car

## Hardware
The project is designed for RP2040 board as it is one of the most available boards ($4) capable of handling multiple PPM inputs.
The built-in LED pin is used for heartbeat monitoring (100 ms tick).

## Usage
**Note!** The project requires serial connection to be established. Before it happens, the code
will remain in dormant mode. A port has to be opened by the client script on the machine.

After serial connection is open, heartbeat will appear at the built-in LED of the RP2040 board.

## Project structure

Directories:

services

data
\-raw

design


## Terms
 - `fubarino` – a common term to define a car

## License
I need to think about it.