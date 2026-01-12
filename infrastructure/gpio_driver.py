try:
    import RPi.GPIO as GPIO
except ImportError:
    GPIO = None


def cleanup():
    GPIO.cleanup()


class GpioDriver:
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)

        self.input_pins = [17, 27]
        self.output_pins = [13, 19, 26]

        for pin in self.input_pins:
            GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        for pin in self.output_pins:
            GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)

    def read(self, gpio: int) -> bool:
        if gpio not in self.input_pins:
            raise ValueError(f"GPIO {gpio} not configured as input")
        return GPIO.input(gpio) == GPIO.HIGH

    def write(self, gpio: int, value: bool):
        if gpio not in self.output_pins:
            raise ValueError(f"GPIO {gpio} not configured as output")
        GPIO.output(gpio, GPIO.HIGH if value else GPIO.LOW)

