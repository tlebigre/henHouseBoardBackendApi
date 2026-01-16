from typing import Protocol


class CurrentSensorPort(Protocol):
    def read_current(self) -> float: ...

    def is_motor_running(self) -> bool: ...