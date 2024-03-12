from datetime import datetime
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, DateTime


Base = declarative_base()


class BaseDbModel(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)
