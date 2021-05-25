import datetime
from typing import *
from pydantic import BaseModel


class ErrorBase(BaseModel):
    test_type: str = None
    test_case: str = None
    error_type: str = None
    error_message: str = None
    traceback: str = None
    stage: str = None
    occurred_at: datetime.datetime


class ErrorCreate(ErrorBase):
    build_id: int


class Error(ErrorBase):
    id: int

    class Config:
        orm_mode = True
