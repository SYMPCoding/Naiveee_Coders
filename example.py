import time
import RPi.GPIO as GPIO
from gas_detection import GasDetection
led_pin=40
buzz_pin=11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led_pin,GPIO.OUT)
GPIO.setup(buzz_pin,GPIO.OUT)

def main():
    """Handle example."""

    print('Calibrating ...')
    detection = GasDetection()

    try:
        while True:
            ppm = detection.percentage()

            print('CO: {} ppm'.format(ppm[detection.CO_GAS]))
            print('H2: {} ppm'.format(ppm[detection.H2_GAS]))
            print('CH4: {} ppm'.format(ppm[detection.CH4_GAS]))
            print('LPG: {} ppm'.format(ppm[detection.LPG_GAS]))
            print('PROPANE: {} ppm'.format(ppm[detection.PROPANE_GAS]))
            print('ALCOHOL: {} ppm'.format(ppm[detection.ALCOHOL_GAS]))
            print('SMOKE: {} ppm\n'.format(ppm[detection.SMOKE_GAS]))

            if ppm[detection.CO_GAS]>0.5 :
                GPIO.output(led_pin,True)
                GPIO.output(buzz_pin,True)
                time.sleep(0.05)
                GPIO.output(led_pin,False)
                GPIO.output(buzz_pin,False)
                time.sleep(0.05)

            time.sleep(0.25)

    except KeyboardInterrupt:
        print('\nAborted by user!')

if __name__ == '__main__':
    main()
