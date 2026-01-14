import asyncio

from domain.models import Engine, DateTimeWithDayOfWeek
from generated import board_pb2_grpc, board_pb2


class BoardServicer(board_pb2_grpc.BoardServicer):

    def __init__(self, gpio_service):
        self.service = gpio_service

    async def GetGpio(self, request, context):
        value = await asyncio.to_thread(
            self.service.get_gpio,
            request.gpio
        )
        return board_pb2.GpioReply(value=value)

    async def SetGpio(self, request, context):
        await asyncio.to_thread(
            self.service.set_gpio,
            request.gpio,
            request.value
        )
        return board_pb2.MessageReply(message="")

    async def GetState(self, request, context):
        value = await asyncio.to_thread(self.service.get_state)
        return board_pb2.StateReply(value=value)

    async def SetState(self, request, context):
        await asyncio.to_thread(self.service.set_state, request.value)
        return board_pb2.MessageReply(message="State updated")

    async def EngineUpOrDown(self, request, context):
        await asyncio.to_thread(
            self.service.engine_up_or_down,
            Engine(
                gpio=request.gpio,
                speed=request.speed,
                button_gpio=request.buttonGpio,
                limit=request.limit,
                is_up=request.isUp,
                is_force=request.isForce,
            )
        )
        return board_pb2.MessageReply(message="")

    async def GetDateTime(self, request, context):
        dt = await asyncio.to_thread(self.service.get_datetime)
        return board_pb2.DateTimeReply(date=dt.date, time=dt.time)

    async def SetDateTime(self, request, context):
        await asyncio.to_thread(
            self.service.set_datetime,
            DateTimeWithDayOfWeek(
                date=request.date,
                time=request.time,
                day_of_week=request.dayOfWeek,
            )
        )
        return board_pb2.MessageReply(message="")
