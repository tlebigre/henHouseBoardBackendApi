class FakeGpioDriver:
    def __init__(self):
        self._state = {}

    def read(self, gpio: int) -> bool:
        return self._state.get(gpio, False)

    def write(self, gpio: int, value: bool):
        self._state[gpio] = value
