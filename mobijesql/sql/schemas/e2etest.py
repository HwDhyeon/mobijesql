import datetime
from pydantic import BaseModel


class E2EtestBase(BaseModel):
    success: int
    failure: int
    skipped: int
    tool: str
    stage: str
    time_start: datetime.datetime
    time_end: datetime.datetime
    time_duration: datetime.time


class E2EtestCreate(E2EtestBase):
    build_id: int


class E2Etest(E2EtestBase):
    id: int

    class Config:
        orm_mode = True
