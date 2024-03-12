from typing import List
from models.leakage import Leakage

from storage.leak_storage import ILeakStorage


class InMemoryLeakStorage(ILeakStorage):
    storage: List[Leakage]

    def __init__(self, storage: List[Leakage]):
        self.storage = storage

    def save_leakage_info(self, data: Leakage):
        self.storage.append(data)

    def get_all_leakeges(self) -> List[Leakage]:
        return self.storage
