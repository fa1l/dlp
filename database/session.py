from sqlalchemy import create_engine

from contextlib import contextmanager
from .base import Base
from sqlalchemy.orm import sessionmaker
from .settings import DBSettings

ENGINE = create_engine(str(DBSettings().url))
metadata = Base.metadata
metadata.bind = ENGINE
Session = sessionmaker(bind=ENGINE, autoflush=True)


@contextmanager
def create_session():
    session = Session(ENGINE)
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
