# FUBAR Labs Autonomous Racing Vehicles

Autonmous Vehicle Project at Fubar Labs for the Autonomous Powerwheels Racing compeition.
* Autonomous Powerwheels Racing Pittsburg Makerfiare 2017
 * We totally did laps. We were on the track on time and ready to go!
* Autonomous Powerwheels Racing Makerfaire NYC 2017
* Autonomous Vehicle Competition via Sparkfun at Denver Makerfaire 2017


## More documentation at the wiki

[Autonomous Project Documenatation](https://github.com/fubarlabs/autonomous/wiki) (outdated)
[Foocars project documentation](https://github.com/fubarlabs/foocars/wiki)

## Code details

Simple model in `basic_model.py`.  Currently linear with mean squared error loss (summed over outputs?)

There is an improved `dropout_model.py` containing a more robust model with a dropout layer.
Otto car includes an experimental `historical_model.py` which uses multiple frames instead of one.

## Inputs

* Webcam image
* Current Accel
* Current Speed

## Future Inputs
* Current Distance from rangefinder
* Current Steering wheel angle

## Outputs

* Steering Wheel angle
* Maybe speed?

# Data sources

* [DeepDrive](http://deepdrive.io)
  * [Compressed subset of DeepDrive](https://drive.google.com/open?id=0B0zbVEese408WjYtWGdJWTF0Rjg)

# Notes
Driving model is in `current_model.py`.  Weights are on [Google Drive](https://goo.gl/D1WmHQ).  Line 74 of the model will have to be changed to reflect the true location/name of the weights file.

There is no need to download models for the first run. They can be taked from Ricarto to make first run. However, training is strongly advised for reliable operations.
