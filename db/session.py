from sqlmodel import Session, create_engine

from contextlib import contextmanager

ENGINE = create_engine("postgresql://postgres:postgres@localhost:5432/dlp")


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
