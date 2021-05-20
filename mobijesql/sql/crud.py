from sqlalchemy.orm import Session
from mobijesql.sql import models
from mobijesql.sql.exceptions import DataNotFoundError
from mobijesql.sql.schemas.error import ErrorCreate
from mobijesql.sql.schemas.build import Build, BuildCreate
from mobijesql.sql.schemas.e2etest import E2EtestCreate


def commit(func):
    def f(*args, **kwargs):
        data = func(*args, **kwargs)
        db = args[0]
        db.commit()
        db.refresh(data)
        return data
    return f


# Build
def get_build(db: Session, build_id: int):
    return db.query(models.Build).filter(models.Build.id == build_id).first()


def get_build_by_info(db: Session, build_name: str, build_number: int):
    return db.query(models.Build).filter(
        models.Build.name == build_name and models.Build.number == build_number
    ).first()


def get_builds(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Build).offset(skip).limit(limit).all()


@commit
def create_build(db: Session, build: BuildCreate):
    db_build = models.Build(**build.dict())
    db.add(db_build)
    return db_build


@commit
def update_build(db: Session, build: Build):
    db_build = db.query(models.Build).filter(
        models.Build.id == build.id
    ).one_or_none()
    if db_build is None:
        raise DataNotFoundError(f'Data not found.(id: {build.id})')

    for var, value in vars(build).items():
        if value:
            setattr(db_build, var, value)

    db.add(db_build)
    return db_build


# E2E
def get_e2e_test(db: Session, test_id: int):
    return db.query(models.E2Etest).filter(
        models.E2Etest.id == test_id
    ).first()


def get_e2e_test_by_build(db: Session, build_id: int):
    return db.query(models.E2Etest).filter(
        models.E2Etest.build_id == build_id
    ).first()


def get_e2e_tests(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.E2Etest).offset(skip).limit(limit).all()


@commit
def create_e2e_test(db: Session, e2etest: E2EtestCreate):
    db_e2etest = models.E2Etest(**e2etest.dict())
    db.add(db_e2etest)
    return db_e2etest


# Errors
def get_errors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Error).offset(skip).limit(limit).all()


def get_error(db: Session, error_id: int):
    return db.query(models.Error).filter(models.Error.id == error_id).first()


def get_errors_by_build(db: Session, build_id: int):
    return db.query(models.Error).filter(
        models.Error.build_id == build_id
    ).all()


@commit
def create_error(db: Session, error: ErrorCreate):
    db_error = models.Error(**error.dict())
    db.add(db_error)
    return db_error
