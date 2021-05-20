import datetime
from typing import *
from pydantic import BaseModel


class BuildBase(BaseModel):
    name: str
    number: int


class BuildCreate(BuildBase):
    time_start: datetime.datetime
    time_end: datetime.datetime
    time_duratioin = datetime.time


class Build(BuildBase):
    id: int

    class Config:
        orm_mode = True
