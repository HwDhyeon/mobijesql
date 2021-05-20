import datetime
from pydantic import BaseModel


class APItestBase(BaseModel):
    success: int
    failure: int
    skipped: int
    tool: str
    stage: str
    time_start: datetime.datetime
    time_end: datetime.datetime
    time_duration: datetime.time


class APItestCreate(APItestBase):
    build_id: int


class APItest(APItestBase):
    id: int

    class Config:
        orm_mode = True
