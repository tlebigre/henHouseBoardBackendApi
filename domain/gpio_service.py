import time
from domain.models import Engine, DateTime, DateTimeWithDayOfWeek
from domain.ports import GpioPort, RtcPort
from infrastructure.state_repository import StateRepository


class GpioService:
    def __init__(
            self,
            gpio_driver: GpioPort,
            state_repo: StateRepository,
            rtc_driver: RtcPort,
    ):
        self.gpio = gpio_driver
        self.state = state_repo
        self.rtc = rtc_driver

    def get_gpio(self, gpio: int) -> bool:
        return self.gpio.read(gpio)

    def set_gpio(self, gpio: int, value: bool):
        self.gpio.write(gpio, value)

    def get_datetime(self) -> DateTime:
        return self.rtc.get_datetime()

    def set_datetime(self, dt: DateTimeWithDayOfWeek):
        self.rtc.set_datetime(dt)

    def get_state(self) -> int:
        return self.state.get()

    def set_state(self, state: int):
        self.state.set(state)

    def engine_up_or_down(self, engine: Engine):
        state = self.state.get()

        while (
                (engine.is_force or self.gpio.read(engine.button_gpio))
                and (state < engine.limit if engine.is_up else state > engine.limit)
        ):
            self.gpio.write(engine.gpio, True)
            time.sleep(0.001 * (6 - engine.speed))
            self.gpio.write(engine.gpio, False)
            time.sleep(0.001 * (5 - engine.speed))

            state += 1 if engine.is_up else -1
            self.state.set(state)
