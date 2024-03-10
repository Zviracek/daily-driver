from dataclasses import dataclass
import datetime


@dataclass(order=True)
class Task:
    date: datetime.date
    time: datetime.time

    name: str
    description: str
    group: str # Grouping by type, for example personal, work

    priority: int
    recuring: bool

    completed: bool


@dataclass(frozen=True, order=True)
class Event:
    start_date: datetime.date
    start_time: datetime.time
    end_date: datetime.date
    end_time: datetime.time

    name: str
    description: str
    group: str # Grouping by type, for example personal, work

    priority: int
    deadline: bool # If True, comparing by end time, probably not realy necessary
    recuring: bool


