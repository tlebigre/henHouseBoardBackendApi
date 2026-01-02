from pydantic import BaseModel


class Engine(BaseModel):
    gpio: int
    speed: int
    button_gpio: int
    limit: int
    is_up: bool
    is_force: bool


class DateTime(BaseModel):
    date: str
    time: str


class DateTimeWithDayOfWeek(DateTime):
    day_of_week: int
