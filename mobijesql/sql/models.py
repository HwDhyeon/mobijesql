import datetime
from sqlalchemy import Column, Integer, String, DateTime, Time, ForeignKey, Text
from sqlalchemy.orm import relationship
from mobijesql.sql.database import Base


CURRENT_TIMESTAMP = datetime.datetime.now()


class Build(Base):
    __tablename__ = 'build'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    number = Column(Integer)
    time_start = Column(DateTime, default=CURRENT_TIMESTAMP)
    time_end = Column(DateTime, default=CURRENT_TIMESTAMP)
    time_duration = Column(Time, default=CURRENT_TIMESTAMP.time())


class CodeStyle(Base):
    __tablename__ = 'code_style'
    id = Column(Integer, primary_key=True, index=True)
    build_id = Column(Integer, ForeignKey('build.id', ondelete='SET NULL'))
    tool = Column(String(30))
    warnings = Column(Integer)
    errors = Column(Integer)
    stage = Column(String(30))
    time_start = Column(DateTime, default=CURRENT_TIMESTAMP)
    time_end = Column(DateTime, default=CURRENT_TIMESTAMP)
    time_duration = Column(Time, default=CURRENT_TIMESTAMP.time())


class Unittest(Base):
    __tablename__ = 'unittest'
    id = Column(Integer, primary_key=True, index=True)
    build_id = Column(Integer, ForeignKey('build.id', ondelete='SET NULL'))
    tool = Column(String(30))
    success = Column(Integer)
    failure = Column(Integer)
    skipped = Column(Integer)
    stage = Column(String(30))
    time_start = Column(DateTime, default=CURRENT_TIMESTAMP)
    time_end = Column(DateTime, default=CURRENT_TIMESTAMP)
    time_duration = Column(Time, default=CURRENT_TIMESTAMP.time())


class APItest(Base):
    __tablename__ = 'apitest'
    id = Column(Integer, primary_key=True, index=True)
    build_id = Column(Integer, ForeignKey('build.id', ondelete='SET NULL'))
    tool = Column(String(30))
    success = Column(Integer)
    failure = Column(Integer)
    skipped = Column(Integer)
    stage = Column(String(30))
    time_start = Column(DateTime, default=CURRENT_TIMESTAMP)
    time_end = Column(DateTime, default=CURRENT_TIMESTAMP)
    time_duration = Column(Time, default=CURRENT_TIMESTAMP.time())


class E2Etest(Base):
    __tablename__ = 'e2etest'
    id = Column(Integer, primary_key=True, index=True)
    build_id = Column(Integer, ForeignKey('build.id', ondelete='SET NULL'))
    tool = Column(String(30))
    success = Column(Integer)
    failure = Column(Integer)
    skipped = Column(Integer)
    stage = Column(String(30))
    time_start = Column(DateTime, default=CURRENT_TIMESTAMP)
    time_end = Column(DateTime, default=CURRENT_TIMESTAMP)
    time_duration = Column(Time, default=CURRENT_TIMESTAMP.time())


class Coverage(Base):
    __tablename__ = 'coverage'
    id = Column(Integer, primary_key=True, index=True)
    build_id = Column(Integer, ForeignKey('build.id', ondelete='SET NULL'))
    tool = Column(String(30))
    coverage = Column(Integer)
    stage = Column(String(30))
    time_start = Column(DateTime, default=CURRENT_TIMESTAMP)
    time_end = Column(DateTime, default=CURRENT_TIMESTAMP)
    time_duration = Column(Time, default=CURRENT_TIMESTAMP.time())


class Error(Base):
    __tablename__ = 'errors'
    id = Column(Integer, primary_key=True, index=True)
    build_id = Column(Integer, ForeignKey('build.id', ondelete='SET NULL'))
    test_type = Column(String(20))
    test_case = Column(String(255))
    error_type = Column(String(255))
    error_message = Column(Text)
    traceback = Column(Text)
    stage = Column(String(30))
    occurred_at = Column(DateTime, default=CURRENT_TIMESTAMP)
