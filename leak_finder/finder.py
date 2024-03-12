from abc import ABC, abstractmethod
from typing import List


class ILeakFinder(ABC):
    @abstractmethod
    def check_for_leaks(self, data: str) -> List[str]:
        pass
