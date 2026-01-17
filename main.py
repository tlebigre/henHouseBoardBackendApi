import asyncio
import os

from grpc import aio

from domain.gpio_service import GpioService
from domain.motor_current_monitor_async import MotorCurrentMonitorAsync
from infrastructure.state_repository import StateRepository
from server.board_servicer import BoardServicer
from generated import board_pb2_grpc

if os.getenv("HARDWARE_MODE") == "raspberry":
    from infrastructure.gpio_driver import GpioDriver
    from infrastructure.acs712_ads1115_driver import ACS712ADS1115Driver
else:
    from infrastructure.fake_gpio_driver import FakeGpioDriver as GpioDriver
    from infrastructure.fake_acs712_ads1115_driver import FakeACS712ADS1115Driver as ACS712ADS1115Driver


async def main():

    monitor = MotorCurrentMonitorAsync(ACS712ADS1115Driver())
    await monitor.start()

    gpio_service = GpioService(
        gpio_driver=GpioDriver(),
        state_repo=StateRepository(),
        current_monitor=monitor
    )

    server = aio.server()
    board_pb2_grpc.add_BoardServicer_to_server(
        BoardServicer(gpio_service), server
    )

    server.add_insecure_port("[::]:9000")
    print("Starting gRPC server on port 9000...")
    await server.start()
    await server.wait_for_termination()
    await monitor.stop()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Server stopped by user")
