import datetime
from typing import *
from pydantic import BaseModel


class ErrorBase(BaseModel):
    test_type: str
    test_case: str
    error_type: str
    error_message: str
    traceback: str
    stage: str
    occurred_at: datetime.datetime


class ErrorCreate(ErrorBase):
    build_id: int


class Error(ErrorBase):
    id: int

    class Config:
        orm_mode = True
