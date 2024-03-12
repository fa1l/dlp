from abc import ABC, abstractmethod
from typing import List
from models.leakage import Leakage


class ILeakStorage(ABC):
    @abstractmethod
    def save_leakage_info(self, data: Leakage):
        pass

    @abstractmethod
    def get_all_leakeges(self) -> List[Leakage]:
        pass
