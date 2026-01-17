import board
import time

try:
    import busio
    import adafruit_ads1x15.ads1115 as ADS
    from adafruit_ads1x15.analog_in import AnalogIn
    print("ACS712ADS1115Driver import is ok")
except ImportError:
    print("ACS712ADS1115Driver import is nok")


class ACS712ADS1115Driver:
    """
    Driver robuste ACS712 + ADS1115 (DC)
    - Calibration automatique du zéro
    - Moyenne glissante
    - Hystérésis ON/OFF
    """

    def __init__(
            self,
            sensitivity=0.185,      # 5A model
            samples=10,             # moyenne glissante
            threshold_on=0.12,      # A -> moteur démarre
            threshold_off=0.06,     # A -> moteur arrêté
            calibration_samples=50
    ):
        self._sensitivity = sensitivity
        self._samples = samples
        self._threshold_on = threshold_on
        self._threshold_off = threshold_off
        self._running = False

        # I2C / ADS1115
        i2c = busio.I2C(board.SCL, board.SDA)
        self._ads = ADS.ADS1115(i2c)
        self._channel = AnalogIn(self._ads, 0)

        # Calibration
        self._zero_voltage = self._calibrate_zero(calibration_samples)

    # ---------------------------------------------------------------------

    def _calibrate_zero(self, n: int) -> float:
        print("[ACS712] Calibration zéro (aucun courant)…")
        time.sleep(2)

        values = [self._channel.voltage for _ in range(n)]
        zero = sum(values) / len(values)

        print(f"[ACS712] Zéro calibré à {zero:.3f} V")
        return zero

    # ---------------------------------------------------------------------

    def _read_current(self) -> float:
        """
        Lecture filtrée du courant (moyenne glissante)
        """
        voltages = [self._channel.voltage for _ in range(self._samples)]
        avg_voltage = sum(voltages) / len(voltages)

        current = (avg_voltage - self._zero_voltage) / self._sensitivity

        print(
            f"[ACS712] Vout={avg_voltage:.3f} V | "
            f"I={current:.2f} A | "
            f"{'ON' if self._running else 'OFF'}"
        )

        return abs(current)

    # ---------------------------------------------------------------------

    def is_motor_running(self) -> bool:
        """
        Détection moteur avec hystérésis
        """
        current = self._read_current()

        if self._running:
            if current < self._threshold_off:
                self._running = False
        else:
            if current > self._threshold_on:
                self._running = True

        return self._running