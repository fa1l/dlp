from re import Pattern
import re
from typing import List
from walrus import Database

from regexp_getter.getter import IRegexpGetter
from regexp_getter.settings import RedisRegexpSettings


class RedisRegexpGetter(IRegexpGetter):
    db: Database
    regexp_key: str

    def __init__(self, redis_settings: RedisRegexpSettings):
        self.db = Database(
            host=redis_settings.host, port=redis_settings.port, db=redis_settings.db
        )
        self.regexp_key = "regexps"

    def add_regexps(self, data: List[Pattern]):
        regexp_storage = self.db.List(self.regexp_key)
        for pattern in data:
            regexp_storage.append(pattern.pattern)

    def remove_regexps(self):
        regexp_storage = self.db.List(self.regexp_key)
        regexp_storage.clear()

    def get_regexps(self) -> List[Pattern]:
        regexps = self.db.List(self.regexp_key)
        regexps.as_list()
        result = []
        for data in regexps:
            regexp = re.compile(str(data, encoding="utf-8"))
            result.append(regexp)
        return result
