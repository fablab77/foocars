import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)


LED_names={ 
  "boot_RPi" : 4,
  "shutdown_RPi" : 3,
  "autonomous" : 27,
  "collect_data" : 2 
}


switch_names={ 
  "thr_step" : 9,
  "autonomous" : 6,
  "collect_data" : 11,
}

 # Switch Testing

for switch in switch_names.values():
    GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_UP)


while True:
    try:
        GPIO.wait_for_edge(switch_names["thr_step"], GPIO.RISING)
        print(f"thr_step: RISING")
        GPIO.wait_for_edge(switch_names["autonomous"], GPIO.RISING)
        print(f"autonomous: RISING")
        GPIO.wait_for_edge(switch_names["collect_data"], GPIO.RISING)
        print(f"colelct_data: RISING")

    finally:
        print("EXIT")
        GPIO.cleanup() # Clean up

