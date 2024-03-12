from typing import List
from leak_finder.finder import ILeakFinder
from models.leakage import Leakage
from regexp_getter.getter import IRegexpGetter


class RegexpLeakFinder(ILeakFinder):
    regexp_getter: IRegexpGetter

    def __init__(self, regexp_getter: IRegexpGetter):
        self.regexp_getter = regexp_getter

    def check_for_leaks(self, data: str) -> List[str]:
        result = []
        for regexp in self.regexp_getter.get_regexps():
            print(regexp)
            if leakage := regexp.search(data):
                message = leakage.group()
                result.append(
                    Leakage(
                        matched_pattern=message,
                        original_message=data,
                        pattern=regexp.pattern,
                    ).model_dump_json()
                )
        return result
