from typing import Protocol


class GpioPort(Protocol):
    def read(self, gpio: int) -> bool: ...

    def write(self, gpio: int, value: bool): ...
