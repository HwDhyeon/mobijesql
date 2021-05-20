import datetime
from pydantic import BaseModels


class CodeStyleBase(BaseModel):
    warnings: int
    errors: int


class CodeStyleCreate(CodeStyleBase):
    build_id: int
    tool: str
    stage: str
    time_start: datetime.datetime
    time_end: datetime.datetime
    time_duration: datetime.time


class CodeStyle(CodeStyleBase):
    id: int

    class Config:
        orm_mode = True
