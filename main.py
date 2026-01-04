import asyncio
import os

from grpc import aio

from domain.gpio_service import GpioService
from infrastructure.state_repository import StateRepository
from server.board_servicer import BoardServicer

if os.getenv("HARDWARE_MODE") == "raspberry":
    from infrastructure.gpio_driver import GpioDriver
    from infrastructure.rtc_driver import RtcDriver
else:
    from infrastructure.fake_gpio_driver import FakeGpioDriver as GpioDriver
    from infrastructure.fake_rtc_driver import FakeRtcDriver as RtcDriver

from generated import board_pb2_grpc as board__pb2_grpc


async def main():
    gpio_service = GpioService(
        gpio_driver=GpioDriver(),
        state_repo=StateRepository(),
        rtc_driver=RtcDriver(),
    )

    server = aio.server()
    board__pb2_grpc.add_BoardServicer_to_server(
        BoardServicer(gpio_service), server
    )

    server.add_insecure_port("127.0.0.1:9000")
    print("Starting gRPC server on port 9000...")
    await server.start()
    await server.wait_for_termination()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Server stopped by user")
