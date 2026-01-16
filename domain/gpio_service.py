import time
from datetime import datetime

from domain.current_sensor_port import CurrentSensorPort
from domain.models import Engine, DateTime, DateTimeWithDayOfWeek
from domain.gpio_ports import GpioPort
from infrastructure.state_repository import StateRepository


class GpioService:
    def __init__(
            self,
            gpio_driver: GpioPort,
            state_repo: StateRepository,
            current_sensor: CurrentSensorPort
    ):
        self._gpio = gpio_driver
        self._state = state_repo
        self._current = current_sensor
        self._now = datetime.now()

    def get_gpio(self, gpio: int) -> bool:
        return self._gpio.read(gpio)

    def set_gpio(self, gpio: int, value: bool):
        self._gpio.write(gpio, value)

    def get_datetime(self) -> DateTime:
        return DateTime(
            date=self._now.strftime("%d/%m/%Y"),
            time=self._now.strftime("%H:%M"),
        )

    def set_datetime(self, dt: DateTimeWithDayOfWeek):
        d, m, y = map(int, dt.date.split("/"))
        h, mi = map(int, dt.time.split(":"))
        self._now = self._now.replace(
            year=y, month=m, day=d, hour=h, minute=mi
        )

    def get_state(self) -> int:
        return self._state.get()

    def set_state(self, state: int):
        self._state.set(state)

    def engine_up_or_down(self, engine: Engine):
        state = self._state.get()

        while (
                (engine.is_force or self._gpio.read(engine.button_gpio))
                and (state < engine.limit if engine.is_up else state > engine.limit)
        ):
            self._gpio.write(engine.gpio, True)
            time.sleep(0.001 * (6 - engine.speed))
            self._gpio.write(engine.gpio, False)
            time.sleep(0.001 * (5 - engine.speed))

            if self._current:
                if not self._current.is_motor_running():
                    continue
        state += 1 if engine.is_up else -1
        self._state.set(state)
