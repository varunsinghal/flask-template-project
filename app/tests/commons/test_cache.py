from unittest import TestCase
from unittest.mock import MagicMock

from cachelib import SimpleCache

from commons.cache import Cache, ttl_cache


class TestCache(TestCase):
    def setUp(self) -> None:
        self.cache_strategy = MagicMock(spec=SimpleCache)
        self.cache = Cache(strategy=self.cache_strategy)

    def test_hashkey(self):
        def demo():
            pass

        actual = self.cache.hashkey(demo, 4, "arg-2")
        expected = "demo.4.arg-2"
        self.assertEqual(actual, expected)

    def test_has(self):
        self.cache_strategy.has.return_value = True
        self.assertTrue(self.cache.has("key"))

    def test_get(self):
        self.cache_strategy.get.return_value = "value"
        self.assertEqual(self.cache.get("key"), "value")

    def test_set(self):
        self.cache_strategy.set.return_value = True
        self.assertTrue(self.cache.set("key", "value"))

    def test_delete(self):
        self.cache_strategy.delete.return_value = True
        self.assertTrue(self.cache.delete("key"))

    def test_clear(self):
        self.cache_strategy.clear.return_value = True
        self.assertTrue(self.cache.clear())


class TestTtlCache(TestCase):
    def setUp(self) -> None:
        self.costly_operation = MagicMock()

    def demo(self, *args):
        self.costly_operation()
        return args

    def test_ttl_cache_with_no_args(self):
        ttl_cache(self.demo)()
        ttl_cache(self.demo)()
        self.costly_operation.assert_called_once()

    def test_ttl_cache_with_same_args(self):
        computed = ttl_cache(self.demo)("arg-1", "arg-2")
        cached = ttl_cache(self.demo)("arg-1", "arg-2")
        self.costly_operation.assert_called_once()
        self.assertEqual(computed, cached)

    def test_ttl_cache_with_different_args(self):
        computed_1 = ttl_cache(self.demo)("arg-1")
        computed_2 = ttl_cache(self.demo)("arg-2")
        self.assertEqual(self.costly_operation.call_count, 2)
        self.assertNotEqual(computed_1, computed_2)
