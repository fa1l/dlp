from db.base import BaseDbModel


class RegexpRule(BaseDbModel, table=True):
    name: str
    regexp: str
