from functools import lru_cache

from leak_finder.regexp import RegexpLeakFinder
from regexp_getter.redis_getter import RedisRegexpGetter
from regexp_getter.settings import RedisRegexpSettings
from storage.in_memory_storage import InMemoryLeakStorage
from independency import Container, ContainerBuilder, Dependency


@lru_cache
def create_container() -> Container:
    builder = ContainerBuilder()
    builder.singleton(
        RedisRegexpGetter, RedisRegexpGetter, redis_settings=RedisRegexpSettings()
    )
    builder.singleton(InMemoryLeakStorage, InMemoryLeakStorage, storage=[])
    builder.singleton(
        RegexpLeakFinder, RegexpLeakFinder, regexp_getter=Dependency(RedisRegexpGetter)
    )
    return builder.build()
