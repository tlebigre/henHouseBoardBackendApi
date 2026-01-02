import time
from domain.models import DateTime, DateTimeWithDayOfWeek

try:
    import board
    import adafruit_ds3231
except ImportError:  # PC / CI / tests
    board = None
    adafruit_ds3231 = None


class RtcDriver:
    def __init__(self):
        if adafruit_ds3231 is None:
            raise RuntimeError("RTC DS3231 not available (not running on Raspberry Pi)")

        i2c = board.I2C()
        self.rtc = adafruit_ds3231.DS3231(i2c)

    def get_datetime(self) -> DateTime:
        date_time = self.rtc.datetime
        return DateTime(
            date=str(date_time.tm_mday).zfill(2) + '/' + str(date_time.tm_mon).zfill(2) + '/' + str(date_time.tm_year),
            time=str(date_time.tm_hour).zfill(2) + ':' + str(date_time.tm_min).zfill(2))

    def set_datetime(self, date_time_with_day_of_week: DateTimeWithDayOfWeek):
        d, m, y = map(int, date_time_with_day_of_week.date.split("/"))
        h, mi = map(int, date_time_with_day_of_week.time.split(":"))

        self.rtc.datetime = time.struct_time(
            (y, m, d, h, mi, 0, date_time_with_day_of_week.day_of_week, -1, -1)
        )
