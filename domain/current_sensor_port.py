from typing import Protocol


class CurrentSensorPort(Protocol):
    def is_motor_running(self) -> bool: ...
