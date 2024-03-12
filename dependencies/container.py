from functools import lru_cache

from leak_finder.regexp import RegexpLeakFinder
from regexp_holder.redis_holder import RedisRegexpHolder
from regexp_holder.settings import RedisRegexpSettings
from storage.in_memory_storage import InMemoryLeakStorage
from independency import Container, ContainerBuilder, Dependency


@lru_cache
def create_container() -> Container:
    builder = ContainerBuilder()
    builder.singleton(
        RedisRegexpHolder, RedisRegexpHolder, redis_settings=RedisRegexpSettings()
    )
    builder.singleton(InMemoryLeakStorage, InMemoryLeakStorage, storage=[])
    builder.singleton(
        RegexpLeakFinder, RegexpLeakFinder, regexp_holder=Dependency(RedisRegexpHolder)
    )
    return builder.build()
