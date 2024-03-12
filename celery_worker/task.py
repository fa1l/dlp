from typing import List
from celery import Task
from leak_finder.finder import ILeakFinder


class LeakFinderTask(Task):
    leak_finder: ILeakFinder
    name = "leak_finder_task"

    def __init__(self, leak_finder: ILeakFinder):
        self.leak_finder = leak_finder

    def run(self, data: str) -> List[str]:
        return self.leak_finder.check_for_leaks(data)
