from database.base import BaseDbModel
from sqlalchemy import Column, String


class DBRegexpRule(BaseDbModel):
    __tablename__ = "regexp_rules"
    name = Column(String, nullable=False)
    regexp = Column(String, nullable=False)
