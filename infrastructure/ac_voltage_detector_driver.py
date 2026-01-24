try:
    import RPi.GPIO as GPIO

    print("GpioDriver import is ok")
except ImportError:
    print("GpioDriver import is nok")


class ACVoltageDetectorDriver:
    def __init__(self, gpio_pin: int = 18):
        self._pin = gpio_pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self._pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        print(f"[AC DETECTOR] GPIO {gpio_pin} prêt")

    def is_motor_running(self) -> bool:
        return GPIO.input(self._pin) == GPIO.LOW

    def cleanup(self):
        GPIO.cleanup(self._pin)
