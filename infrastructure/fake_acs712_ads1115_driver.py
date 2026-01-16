
class FakeACS712ADS1115Driver:
    def __init__(
            self,
            sensitivity=0.185,
            zero_voltage=2.46,
            threshold=0.1,
            consecutive=3
    ):
        self._sensitivity = sensitivity
        self._zero_voltage = zero_voltage
        self._threshold = threshold
        self._consecutive = consecutive
        self._history = []

    def read_current(self) -> float:
        return 0.2

    def is_motor_running(self) -> bool:
        return True