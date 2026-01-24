import unittest
import os
import tempfile
from domain.gpio_service import GpioService
from domain.models import Engine
from infrastructure.fake_gpio_driver import FakeGpioDriver
from infrastructure.state_repository import StateRepository


class DummyMonitor:
    def is_motor_running(self):
        return True


class TestEngine(unittest.TestCase):
    def _run_engine_test(self, initial_state, limit, is_up, expected_state):
        tmp = tempfile.NamedTemporaryFile(delete=False)
        tmp.close()
        try:
            gpio = FakeGpioDriver()
            state = StateRepository(path=tmp.name)
            monitor = DummyMonitor()
            service = GpioService(gpio, state, monitor)

            state.set(initial_state)
            service.engine_up_or_down(
                Engine(
                    gpio=13,
                    speed=3,
                    button_gpio=17,
                    limit=limit,
                    is_up=is_up,
                    is_force=True,
                )
            )
            assert state.get() == expected_state
        finally:
            os.unlink(tmp.name)

    def test_engine_up(self):
        self._run_engine_test(initial_state=0, limit=5, is_up=True, expected_state=5)

    def test_engine_down(self):
        self._run_engine_test(initial_state=5, limit=0, is_up=False, expected_state=0)

    def test_engine_up_already_at_limit(self):
        self._run_engine_test(initial_state=5, limit=5, is_up=True, expected_state=5)

    def test_engine_down_already_at_limit(self):
        self._run_engine_test(initial_state=0, limit=0, is_up=False, expected_state=0)


if __name__ == "__main__":
    unittest.main()
