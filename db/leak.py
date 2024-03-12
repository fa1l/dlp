from db.base import BaseDbModel


class DBLeakage(BaseDbModel, table=True):
    message: str
    content: str
    pattern: str
