from abc import ABC, abstractmethod
from re import Pattern
from typing import List


class IRegexpHolder(ABC):
    @abstractmethod
    def get_regexps(self) -> List[Pattern]:
        pass

    @abstractmethod
    def add_regexps(self, data: List[Pattern]):
        pass

    @abstractmethod
    def remove_regexps(self):
        pass
