import board

try:
    import busio
    import adafruit_ads1x15.ads1115 as ADS
    from adafruit_ads1x15.analog_in import AnalogIn
    print("ACS712ADS1115Driver import is ok")
except ImportError:
    print("ACS712ADS1115Driver import is nok")


class ACS712ADS1115Driver:
    def __init__(self, samples=100, threshold_mv=8):
        self._threshold = threshold_mv / 1000.0

        i2c = busio.I2C(board.SCL, board.SDA)
        self._ads = ADS.ADS1115(i2c)
        self._channel = AnalogIn(self._ads, 0)

        self._zero = self._calibrate_zero(samples)

    def _calibrate_zero(self, samples):
        values = [self._channel.voltage for _ in range(samples)]
        zero = sum(values) / len(values)
        print(f"[ACS712] Zero calibrated at {zero:.3f} V")
        return zero

def is_motor_running(self) -> bool:
    delta = abs(self._channel.voltage - self._zero)
    print(f"ΔV={delta*1000:.1f} mV")
    return delta > self._threshold