import board

try:
    import busio
    import adafruit_ads1x15.ads1115 as ADS
    from adafruit_ads1x15.analog_in import AnalogIn
    print("ACS712ADS1115Driver import is ok")
except ImportError:
    print("ACS712ADS1115Driver import is nok")


class ACS712ADS1115Driver:
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

        i2c = busio.I2C(board.SCL, board.SDA)
        self._ads = ADS.ADS1115(i2c)
        self._channel = AnalogIn(self._ads, ADS.P0)

    def read_current(self) -> float:
        voltage = self._channel.voltage
        current = (voltage - self._zero_voltage) / self._sensitivity
        return current

    def is_motor_running(self) -> bool:
        current = abs(self.read_current())
        self._history.append(current > self._threshold)

        if len(self._history) > self._consecutive:
            self._history.pop(0)

        return self._history.count(True) == self._consecutive