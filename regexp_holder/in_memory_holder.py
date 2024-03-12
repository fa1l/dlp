from re import Pattern
from typing import List

from regexp_holder.holder import IRegexpHolder


class InMemoryRegexpHolder(IRegexpHolder):
    storage: List[Pattern]

    def __init__(self, storage: List[Pattern]):
        self.storage = storage

    def get_regexps(self) -> List[Pattern]:
        return self.storage

    def add_regexps(self, data: List[Pattern]):
        self.storage.extend(data)

    def remove_regexps(self):
        self.storage.clear()
