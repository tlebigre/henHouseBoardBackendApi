from domain.gpio_service import GpioService
from domain.models import Engine
from domain.motor_current_monitor_async import MotorCurrentMonitorAsync
from infrastructure.fake_gpio_driver import FakeGpioDriver
from infrastructure.fake_acs712_ads1115_driver import FakeACS712ADS1115Driver
from infrastructure.state_repository import StateRepository


def test_engine_up():
    gpio = FakeGpioDriver()
    state = StateRepository(path=":memory:")
    monitor = MotorCurrentMonitorAsync(FakeACS712ADS1115Driver())
    service = GpioService(gpio, state, monitor)

    service.engine_up_or_down(
        Engine(
            gpio=13,
            speed=3,
            button_gpio=17,
            limit=5,
            is_up=True,
            is_force=True,
        )
    )

    assert state.get() == 5
