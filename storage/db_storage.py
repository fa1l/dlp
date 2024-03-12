from typing import List
import database
from database.leak import DBLeakage
from models.leakage import Leakage
from sqlmodel import select

from storage.leak_storage import ILeakStorage


class DBLeakStorage(ILeakStorage):
    def save_leakage_info(self, data: Leakage):
        db_leakage = DBLeakage(
            message=data.message, content=data.content, pattern=data.pattern
        )
        with database.create_session() as session:
            session.add(db_leakage)

    def get_all_leakeges(self) -> List[Leakage]:
        with database.create_session() as session:
            statement = select(DBLeakage)
            db_leakages = session.exec(statement).all()
            result = [
                Leakage(
                    mesasage=db_leak.message,
                    context=db_leak.content,
                    pattern=db_leak.pattern,
                )
                for db_leak in db_leakages
            ]

            return result
