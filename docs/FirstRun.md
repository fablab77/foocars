# Running the code from the repo
Before running the code, one has to make a decision about the specific car and interface hardware (see [Hardware]()).
It can be advised to make a copy of `templatecar` and proceed on that basis.
The interface code has been recently tested with Teensy 3.2 and Fubarino SD; Arduino Pro Micro (Leonardo-compatible) version is WIP.

## Car Code

### Preparing to flash the interface

The code is installed on the Raspberry PI using Platform IO
```python2.7
sudo pip install platformio
```
Platform IO is only Python 2.7 but it can program the Arduino. In our case it's the Fubarion SD board.

### Flashing the interface

This part depends on the interface hardware chosen.

Arduino code location: `./foocars/cars/<car_name>/arduino`
```
cd arduino

```
MOTTO: Small RC Car
Collection Code: MOTTOServoDtaSampleDelay.ino

```
cd MOTTOServoDataSampleDelay
pio run -t upload
```
Full Auto Code: MOTTOFullAutoDrive.ino

```
cd MOTTOFUllAutoDrive.ino
pio run -t upload
```

OTTO: Power Wheels Autonomus
Collection Code: NewOTTOFullAutoDrive.ino
```
cd NewOTTOFUllAutoDrive.ino
pio run -t upload
```
Full Auto Code:  NewOTTOFullAutoDrive.ino
```
cd NewOTTOFUllAutoDrive.ino
pio run -t upload
```


### Preparing your PI

```
sudo apt-getupdate
sudo apt-get install python3-pip python3-dev ython3-dev python3-pip python-pip python3-h5py \
python3-numpy python3-matplotlib python3-scipy python3-pandas 
```
Get TensorFlow for PI installed (http://www.instructables.com/id/Google-Tensorflow-on-Rapsberry-Pi/)
```
wget https://github.com/samjabrahams/tensorflow-on-raspberry-pi/releases/download/v1.1.0/tensorflow-1.1.0-cp34-cp34m-linux_armv7l.whl
```
Install Tensorflow for Python 3.4
```
sudo pip3 install pip3 install tensorflow-1.1.0-cp34-cp34m-linux_armv7l.whl 
```
If you have Tensorflow on Raspberry PI with Stretch you need to rename the Tensorflow wheel binary:

```
cp tensorflow-1.1.0-cp34-cp34m-linux_armv7l.whl tensorflow-1.1.0-cp35-cp35m-linux_armv7l.whl
```

Fix a potential error message:
```
sudo pip3 uninstall mock
sudo pip3 install mock
```
Install the Python libraries:

```
git clone https://github.com/fubarlabs/foocars
cd foocars
virtualenv auto -p python3 
source auto/bin/activate
pip install -r requirements.txt
```

### Optional: set up the services to be launched at startup
Set up the Raspberry Pi services
```
cd /usr/local/bin
ln -s ~/foocars/services/ottoMicroLogger.py
ln -s ~/foocars/services/ottoMicroLogger.service
systemctl enable ~/foocars/services/ottoMicroLogger.service
```

## Running the code
By default, the interface firmware does not pass manual control (R/C remote to servo and motor ESC).

Run the code by typing
```
cd ~/foocars/<your_car>/services
# Create directory for data
mkdir ../data
mkdir ../data/collected
mkdir ../data/weights
# Copy pretrained weights
cp ../../ricarto/weights/* ../data/weights
# Copy the pretrained model
cp ../../ricarto/services/dropout_model.py .
python3 carRunner.py
```

**Note:** After everything is set up, the code will operate in **Manual** mode.
It may be switched to **Learning** or **Self-driving** modes by turning the corresponding switches.
Please note that both modes are turned off by default; in case the switch is on when the code is launched, you will need to turn it off and then back on to activate the mode.