import os
import sqlalchemy
from sqlalchemy.orm import sessionmaker


def __get_url():
    return "postgresql://%s:%s@%s/%s" % (
        os.environ.get("POSTGRES_USER"),
        os.environ.get("POSTGRES_PASSWORD"),
        os.environ.get("POSTGRES_HOST"),
        os.environ.get("POSTGRES_DB"),
    )


def __db_session():
    db_url = __get_url()
    engine = sqlalchemy.create_engine(db_url)
    return sessionmaker(bind=engine, autoflush=True)()


def get_session():
    try:
        db = __db_session()
        yield db
    finally:
        db.close()