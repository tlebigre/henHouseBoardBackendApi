try:
    import RPi.GPIO as GPIO
    print("GpioDriver import is ok")
except ImportError:
    print("GpioDriver import is nok")


def cleanup():
    GPIO.cleanup()


class GpioDriver:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        self._input_pins = [17, 27]
        self._output_pins = [13, 19, 26]

        for pin in self._input_pins:
            GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        for pin in self._output_pins:
            GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)

    def read(self, gpio: int) -> bool:
        if gpio not in self._input_pins:
            raise ValueError(f"GPIO {gpio} not configured as input")
        return GPIO.input(gpio) == GPIO.HIGH

    def write(self, gpio: int, value: bool):
        if gpio not in self._output_pins:
            raise ValueError(f"GPIO {gpio} not configured as output")
        GPIO.output(gpio, GPIO.HIGH if value else GPIO.LOW)

