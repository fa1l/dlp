from functools import lru_cache
import re

from leak_finder.regexp import RegexpLeakFinder
from storage.in_memory_storage import InMemoryLeakStorage
from independency import Container, ContainerBuilder


@lru_cache
def create_container() -> Container:
    builder = ContainerBuilder()
    builder.singleton(InMemoryLeakStorage, InMemoryLeakStorage, storage=[])
    builder.singleton(
        RegexpLeakFinder,
        RegexpLeakFinder,
        regexp_storage=[re.compile("aab"), re.compile("bcd")],
    )
    return builder.build()
