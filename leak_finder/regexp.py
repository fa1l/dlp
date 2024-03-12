from re import Pattern
from typing import List
from leak_finder.finder import ILeakFinder
from models.leakage import Leakage


class RegexpLeakFinder(ILeakFinder):
    regexp_storage: List[Pattern]

    def __init__(self, regexp_storage: List[Pattern]):
        self.regexp_storage = regexp_storage

    def check_for_leaks(self, data: str) -> List[str]:
        result = []
        for regexp in self.regexp_storage:
            if leakage := regexp.search(data):
                message = leakage.group()
                result.append(
                    Leakage(
                        message=message, content=data, pattern=regexp.pattern
                    ).model_dump_json()
                )
        return result
