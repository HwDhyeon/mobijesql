from sqlalchemy.orm import Session
from mobijesql.sql import crud, models, schemas
from mobijesql.sql.database import SessionLocal, engine
from mobijesql.sql.exceptions import DataDuplicatedError
from mobijesql.sql.exceptions import DataNotFoundError


models.Base.metadata.create_all(bind=engine)
a_db = SessionLocal()


def close():
    a_db.close()


def read_builds(skip: int = 0, limit: int = 100, db: Session = a_db):
    builds = crud.get_builds(db, skip=skip, limit=limit)
    if not builds:
        raise DataNotFoundError('데이터가 없습니다.')
    return builds


def create_build(build: schemas.build.BuildCreate, db: Session = a_db):
    db_build = crud.get_build_by_info(db, build_name=build.name, build_number=build.number)
    if db_build:
        raise DataDuplicatedError(f'{build.name}의 {build.number}번 빌드는 이미 존재합니다.')
    return crud.create_build(db=db, build=build)


def read_e2e_tests(skip: int = 0, limit: int = 100, db: Session = a_db):
    tests = crud.get_e2e_tests(db, skip=skip, limit=limit)
    if not tests:
        raise DataNotFoundError('데이터가 없습니다.')
    return tests


def create_e2e_test(e2etest: schemas.e2etest.E2EtestCreate, db: Session = a_db):
        db_e2etest = crud.get_e2e_test_by_build(db, e2etest.build_id)
        if db_e2etest and db_e2etest.stage == e2etest.stage:
            raise DataDuplicatedError(f'{build.name}의 {build.number}번 빌드는 이미 존재합니다.')
        return crud.create_e2e_test(db, e2etest=e2etest)
