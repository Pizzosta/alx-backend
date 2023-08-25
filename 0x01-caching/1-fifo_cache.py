#!/usr/bin/python3
""" FIFOCache module
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache class that inherits from BaseCaching"""

    def __init__(self):
        """ Initiliaze the FIFOCache instance"""
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache"""
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                first_in_key = next(iter(self.cache_data))
                print("DISCARD:", first_in_key)
                del self.cache_data[first_in_key]
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
