import datetime
from typing import *
from pydantic import BaseModel


class ErrorBase(BaseModel):
    test_type: str
    test_case: str
    error_type: str
    traceback: str


class ErrorCreate(ErrorBase):
    build_id: int
    stage: str
    occurred_at: datetime.datetime


class Error(ErrorBase):
    id: int

    class Config:
        orm_mode = True
