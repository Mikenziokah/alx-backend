#!/usr/bin/python3
"""class LIFOCache that inherits from BaseCaching and is a
    caching system
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ a lifo caching system that inherits from the basecache
    """
    def __init__(self):
        """ initialize
        """
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """ adding items in the cache
        """
        if key is None and item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discarded_key = self.stack.pop()
            del self.cache_data[discarded_key]
            print("DISCARD:", discarded_key)

        self.stack.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """Retrieve an item from the cache
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
