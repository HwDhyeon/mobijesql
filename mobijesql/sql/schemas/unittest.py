import datetime
from pydantic import BaseModel


class UnittestBase(BaseModel):
    success: int
    failure: int
    skipped: int


class UnittestCreate(UnittestBase):
    build_id: int
    tool: str
    stage: str
    time_start: datetime.datetime
    time_end: datetime.datetime
    time_duration: datetime.time


class Unittest(UnittestBase):
    id: int

    class Config:
        orm_mode = True
