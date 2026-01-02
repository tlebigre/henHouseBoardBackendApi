from datetime import datetime
from domain.models import DateTime, DateTimeWithDayOfWeek


class FakeRtcDriver:
    def __init__(self):
        self._now = datetime.now()

    def get_datetime(self) -> DateTime:
        return DateTime(
            date=self._now.strftime("%d/%m/%Y"),
            time=self._now.strftime("%H:%M"),
        )

    def set_datetime(self, dt: DateTimeWithDayOfWeek):
        d, m, y = map(int, dt.date.split("/"))
        h, mi = map(int, dt.time.split(":"))
        self._now = self._now.replace(
            year=y, month=m, day=d, hour=h, minute=mi
        )
