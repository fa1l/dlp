from typing import List
from leak_finder.finder import ILeakFinder
from models.leakage import Leakage
from regexp_holder.holder import IRegexpHolder


class RegexpLeakFinder(ILeakFinder):
    regexp_holder: IRegexpHolder

    def __init__(self, regexp_holder: IRegexpHolder):
        self.regexp_holder = regexp_holder

    def check_for_leaks(self, data: str) -> List[str]:
        result = []
        for regexp in self.regexp_holder.get_regexps():
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
