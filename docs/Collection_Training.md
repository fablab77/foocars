# Data collection and training
Training is required to fit performance of a specific sample to the needs of a user.

Currently the models map one or two parameters (steering angle and, in some models, motor power) to situation on one or a sequence (historical model in Otto car) frames achieved from the camera.

The 

## Data Collection Code (obsolete)
Data collection is done as a Raspberry PI service. The folder services contains:
1. ottologger.py
2. ottologger.service

1. Copy ottologger.py /usr/local/bin
2. register ottologer.service as a system service
3. Switch on pin 4 enables and disables collection
4. LED on pin 11 shows the status of collection

## Data collection (current)
Run the services [following the instructions](). Switch to learning mode. The car will start saving the data into `~/cars/<your_car>/data/collected` directory.

The data has the following format:
1. `commands_<timestamp>.npz` - a packet containing commands (steering and speed) received over radio channel from the operator;
2. `IMU_<timestamp>.npz` 
3. `imgs_<timestamp>.npz`

All the packets are synchronized.

## Training
The following operations may be performed both on target car and on a PC. Training on the target car is not advised, as it will take way longer than on a normal machine, but it is possible.

### Optional step: cleaning up
There is a useful utility, `curator`, developed to review data collected and check the video.


### Training code

### Troubleshooting
In case the training process fails with `Error: cannot decompress the zipped data`, it means that one of the data packets has been corrupted. That might happen if Python code was terminated, or the SD card in Raspberry has writing issues. Run the following command to try unpacking the code: 
``` for f in *.npz; do unzip $f && rm arr_0.npy; done```

Simply remove the packet corrupted (do not forget to throw away commands, IMU and images data at the same time!).