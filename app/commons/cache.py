import functools
import logging
from abc import ABC, abstractmethod
from typing import Optional

from cachelib import SimpleCache

logger = logging.getLogger(__name__)


class ICache(ABC):
    """
    Cache interface used to define the template for the rest
    of the code. The adaptor can be used to adapt to other
    implementations without impacting the cache behavior.
    """

    @abstractmethod
    def hashkey(self, func, *args):
        pass

    @abstractmethod
    def has(self, key):
        pass

    @abstractmethod
    def get(self, key):
        pass

    @abstractmethod
    def set(self, key, value):
        pass

    @abstractmethod
    def delete(self, key):
        pass

    @abstractmethod
    def clear(self):
        pass


class CacheAdaptor(ICache):
    def __init__(self, adaptee) -> None:
        self.adaptee = adaptee

    def hashkey(self, func, *args):
        args_key = ".".join(map(lambda x: str(x), args))
        return func.__name__ + "." + args_key

    def has(self, key):
        return self.adaptee.has(key)

    def get(self, key):
        return self.adaptee.get(key)

    def set(self, key, value):
        return self.adaptee.set(key, value)

    def delete(self, key):
        return self.adaptee.delete(key)

    def clear(self):
        return self.adaptee.clear()


_cache = CacheAdaptor(adaptee=SimpleCache(threshold=300, default_timeout=20))


def ttl_cache(func, cache_cls: Optional[ICache] = _cache):
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
