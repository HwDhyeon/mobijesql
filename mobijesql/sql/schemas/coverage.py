import datetime
from pydantic import BaseModel


class CoverageBase(BaseModel):
    coverage: int
    tool: str
    stage: str
    time_start: datetime.datetime
    time_end: datetime.datetime
    time_duration: datetime.time


class CoverageCreate(CoverageBase):
    build_id: int


class Coverage(CoverageBase):
    id: int

    class Config:
        orm_mode = True
