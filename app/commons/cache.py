import functools
import logging
from typing import Optional

from cachelib import SimpleCache

logger = logging.getLogger(__name__)


class Cache:
    """
    Cache class used to interact with the rest of the code.
    The strategy can be replaced with other implementations
    without impacting the cache behavior.
    """

    def __init__(self, strategy) -> None:
        self.strategy = strategy

    def hashkey(self, func, *args):
        args_key = ".".join(map(lambda x: str(x), args))
        return func.__name__ + "." + args_key

    def has(self, key):
        return self.strategy.has(key)

    def get(self, key):
        return self.strategy.get(key)

    def set(self, key, value):
        return self.strategy.set(key, value)

    def delete(self, key):
        return self.strategy.delete(key)

    def clear(self):
        return self.strategy.clear()


_cache = Cache(strategy=SimpleCache(threshold=300, default_timeout=20))


def ttl_cache(func, cache_cls: Optional[Cache] = _cache):
    """
    Cache the output of the function provided in `func`.
    Builds the key using the function name and arguments provided.
    The default timeout for the cache is 20 seconds.
    The optional `cache_cls` is provided to override the behavior with
    other cache utility.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = cache_cls.hashkey(func, *args)
        if cache_cls.has(key):
            return cache_cls.get(key)
        value = func(*args, **kwargs)
        cache_cls.set(key, value)
        return value

    return wrapper
