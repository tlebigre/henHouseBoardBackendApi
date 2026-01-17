class FakeACS712ADS1115Driver:
    def __init__(self):
        self._running = True

    def set_running(self, value: bool):
        self._running = value

    def is_motor_running(self) -> bool:
        return self._running
