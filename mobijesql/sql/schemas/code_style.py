import datetime
from pydantic import BaseModels


class CodeStyleBase(BaseModel):
    warnings: int
    errors: int
    tool: str
    stage: str
    time_start: datetime.datetime
    time_end: datetime.datetime
    time_duration: datetime.time


class CodeStyleCreate(CodeStyleBase):
    build_id: int


class CodeStyle(CodeStyleBase):
    id: int

    class Config:
        orm_mode = True
