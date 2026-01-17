import asyncio

from domain.current_sensor_port import CurrentSensorPort


class MotorCurrentMonitorAsync:
    def __init__(self, sensor: CurrentSensorPort, interval=0.05):
        self._sensor = sensor
        self._interval = interval
        self._motor_running = False
        self._task = None
        self._stop_event = asyncio.Event()

    async def start(self):
        self._task = asyncio.create_task(self._loop())

    async def stop(self):
        self._stop_event.set()
        if self._task:
            await self._task

    async def _loop(self):
        while not self._stop_event.is_set():
            self._motor_running = await asyncio.to_thread(
                self._sensor.is_motor_running
            )
            await asyncio.sleep(self._interval)

    def is_motor_running(self) -> bool:
        return self._motor_running
