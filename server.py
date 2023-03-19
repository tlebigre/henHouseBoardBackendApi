import grpc
from concurrent import futures
import time

#import the generated files
import board_pb2 as board_pb2
import board_pb2_grpc as board_pb2_grpc

#import the function files
import gpioBoard

class BoardServicer(board_pb2_grpc.BoardServicer):

    def GetGpio(self, request, context):
        return board_pb2.GpioReply(value=gpioBoard.getGpio(request.gpio))

    def SetGpio(self, request, context):
        gpioBoard.setGpio(request.gpio, request.value)
        return board_pb2.MessageReply(message="")

    def GetState(self, request, context): 
        return board_pb2.StateReply(value=gpioBoard.getState())
        
    def SetState(self, request, context):
        gpioBoard.setState(request.value)
        return board_pb2.MessageReply(message="")
        
    def GetDateTime(self, request, context):
        dateTime = gpioBoard.getDateTime()
        return board_pb2.DateTimeReply(date=dateTime.date,time=dateTime.time)
        
    def SetDateTime(self, request, context):
        gpioBoard.setDateTime(gpioBoard.DateTimeWithDayOfWeek(
        date=request.date, time = request.time, dayOfWeek = request.dayOfWeek))
        return board_pb2.MessageReply(message="")
        
    def EngineUpOrDown(self, request, context):
        gpioBoard.engineUpOrDown(gpioBoard.Engine(
        gpio = request.gpio,
        speed = request.speed,
        buttonGpio = request.buttonGpio,
        limit = request.limit,
        isUp = request.isUp,
        isForce = request.isForce))
        return board_pb2.MessageReply(message="")

#create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
board_pb2_grpc.add_BoardServicer_to_server(BoardServicer(), server)
server.add_insecure_port('127.0.0.1:9000')
server.start()
server.wait_for_termination()