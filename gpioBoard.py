from pydantic import BaseModel
import RPi.GPIO as GPIO
import time
import adafruit_ds3231
import board

i2c = board.I2C()
rtc = adafruit_ds3231.DS3231(i2c)
GPIO.setwarnings(False)

#--------------------
#-- init GPIO -------
#-------------------- 
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(19, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(26, GPIO.OUT, initial=GPIO.LOW)

#--------------------
#-- GPIO ------------
#-------------------- 
def getGpio(gpio: int):
    return GPIO.input(gpio)
 
def setGpio(gpio: int, value: bool):
    if value:
        GPIO.output(gpio, GPIO.HIGH)
    else:
        GPIO.output(gpio, GPIO.LOW)

#--------------------
#-- Engine ----------
#--------------------    
class Engine(BaseModel):
    gpio: int
    speed: int
    buttonGpio : int
    limit: int
    isUp: bool
    isForce: bool

def engineUpOrDown(engine : Engine):
    state = getState()
    while ((engine.isForce or GPIO.input(engine.buttonGpio)) 
    and ((state < engine.limit) if engine.isUp else (state > engine.limit))):
        GPIO.output(engine.gpio, GPIO.HIGH)
        time.sleep(0.001*(6-engine.speed))
        GPIO.output(engine.gpio, GPIO.LOW)
        time.sleep(0.001*(5-engine.speed))
        if engine.isUp :
            state += 1
        else :
            state -= 1
        setState(state)

#--------------------
#-- State -----------
#--------------------    
def getState():
    with open('state.txt') as f:
        content = f.read()
        return 0 if (content == "") else int(content)

def setState(state : int) :
    with open('state.txt', 'w') as f:
        f.write(str(state))

#--------------------
#-- DateTime --------
#--------------------
class DateTime(BaseModel):
    date: str
    time: str
   
class DateTimeWithDayOfWeek(BaseModel):
    date: str
    time: str
    dayOfWeek : int

def getDateTime() -> DateTime :
    dateTime = rtc.datetime
    return DateTime(date=str(dateTime.tm_mday).zfill(2)+'/'+str(dateTime.tm_mon).zfill(2)+'/'+str(dateTime.tm_year), 
        time=str(dateTime.tm_hour).zfill(2)+':'+str(dateTime.tm_min).zfill(2))

def setDateTime(dateTimeWithDayOfWeek : DateTimeWithDayOfWeek):
    splitDate = dateTimeWithDayOfWeek.date.split('/')
    splitTime = dateTimeWithDayOfWeek.time.split(':')
    rtc.datetime = time.struct_time((
        int(splitDate[2]), int(splitDate[1]), int(splitDate[0]),
        int(splitTime[0]), int(splitTime[1]), 0,
        int(dateTimeWithDayOfWeek.dayOfWeek), -1, -1))