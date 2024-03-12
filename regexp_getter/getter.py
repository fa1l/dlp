from abc import ABC, abstractmethod
from re import Pattern
from typing import List


class IRegexpGetter(ABC):
    @abstractmethod
    def get_regexps(self) -> List[Pattern]:
        pass
