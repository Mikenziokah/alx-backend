#!/usr/bin/python3
""" class LFUCache that inherits from BaseCaching
    and is a caching system
"""
BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(Basecache):
    """ lfucahe from basecache
    """
    def __init__(self):
        """ intialize
        """
        super().__init__()
        self.occur = dict

    def put(self, key, item):
        """ adding items in the cache
        """
        if key is None and item is None:
            return

    def get(self, key):
        """ Get an item by key """
        if(key is None or key not in self.cache_data.keys()):
            return
        self.uses[key] += 1
        return self.cache_data.get(key)
