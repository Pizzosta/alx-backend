#!/usr/bin/python3
""" LIFOCache module
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache class that inherits from BaseCaching"""

    def __init__(self):
        """ Initiliaze the LIFOCache instance"""
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache"""
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                last_in_key = list(self.cache_data.keys())[-1]
                print("DISCARD:", last_in_key)
                del self.cache_data[last_in_key]
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
