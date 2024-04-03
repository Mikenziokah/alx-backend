#!/usr/bin/python3
""" class FIFOCache that inherits from BaseCaching
    and is a caching system
"""

BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache that inherits from BaseCaching
    """
    def __init__(self):
        """ intialize
        """
        super(). __init__()
        self.queue = []

    def put(self, key, item):
        """adding items in the cache
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discarded_key = self.queue.pop(0)
            del self.cache_data[discarded_key]
            print("DISCARD:", discarded_key)

        self.queue.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """Retrieve an item from the cache"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
