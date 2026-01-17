import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn


class ACS712ADS1115Driver:
    """
    Driver ACS712 + ADS1115 DC
    - Calibration zéro
    - Moyenne glissante
    - Hystérésis
    - Option inversion logique
    """

    def __init__(
            self,
            sensitivity=0.185,
            samples=10,
            threshold_on=0.12,
            threshold_off=0.06,
            calibration_samples=50,
            inverted=True   # 🔥 IMPORTANT
    ):
        self._sensitivity = sensitivity
        self._samples = samples
        self._threshold_on = threshold_on
        self._threshold_off = threshold_off
        self._inverted = inverted

        self._running = False

        i2c = busio.I2C(board.SCL, board.SDA)
        self._ads = ADS.ADS1115(i2c)
        self._channel = AnalogIn(self._ads, ADS.P0)

        self._zero_voltage = self._calibrate_zero(calibration_samples)

    # ------------------------------------------------------------

    def _calibrate_zero(self, n: int) -> float:
        print("[ACS712] Calibration zéro (aucun courant)…")
        time.sleep(2)

        values = [self._channel.voltage for _ in range(n)]
        zero = sum(values) / len(values)

        print(f"[ACS712] Zéro calibré à {zero:.3f} V")
        return zero

    # ------------------------------------------------------------

    def _read_current(self) -> float:
        voltages = [self._channel.voltage for _ in range(self._samples)]
        avg_voltage = sum(voltages) / len(voltages)

        current = (avg_voltage - self._zero_voltage) / self._sensitivity
        current = abs(current)

        # inversion logique si nécessaire
        effective_current = -current if self._inverted else current

        print(
            f"[ACS712] Vout={avg_voltage:.3f} V | "
            f"I={effective_current:.2f} A | "
            f"{'ON' if self._running else 'OFF'}"
        )

        return effective_current

    # ------------------------------------------------------------

    def is_motor_running(self) -> bool:
        current = self._read_current()

        if self._running:
            if current < self._threshold_off:
                self._running = False
        else:
            if current > self._threshold_on:
                self._running = True

        return self._running
