from database.base import BaseDbModel
from sqlalchemy import Column, String


class DBLeakage(BaseDbModel):
    __tablename__ = "leakage"
    message = Column(String, nullable=False)
    content = Column(String, nullable=False)
    pattern = Column(String, nullable=False)
