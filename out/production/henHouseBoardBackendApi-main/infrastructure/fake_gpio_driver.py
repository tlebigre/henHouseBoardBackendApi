class FakeGpioDriver:
    def __init__(self):
        self.state = {}

    def read(self, gpio: int) -> bool:
        return self.state.get(gpio, False)

    def write(self, gpio: int, value: bool):
        self.state[gpio] = value
