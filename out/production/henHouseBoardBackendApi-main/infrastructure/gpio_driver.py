from gpiozero import DigitalInputDevice, DigitalOutputDevice


class GpioDriver:
    def __init__(self):
        # GPIO configurés en entrée (pull-down)
        self.inputs = {
            17: DigitalInputDevice(17, pull_up=False),
            27: DigitalInputDevice(27, pull_up=False),
        }

        # GPIO configurés en sortie
        self.outputs = {
            13: DigitalOutputDevice(13, initial_value=False),
            19: DigitalOutputDevice(19, initial_value=False),
            26: DigitalOutputDevice(26, initial_value=False),
        }

    def read(self, gpio: int) -> bool:
        if gpio not in self.inputs:
            raise ValueError(f"GPIO {gpio} not configured as input")
        return self.inputs[gpio].value

    def write(self, gpio: int, value: bool):
        if gpio not in self.outputs:
            raise ValueError(f"GPIO {gpio} not configured as output")
        self.outputs[gpio].value = value
