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
        self.que = ()

    def put(self, key, item):
        """adding items in the cache
        """

