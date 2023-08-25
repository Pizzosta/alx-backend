#!/usr/bin/python3
""" BaseCaching module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BaseCache class that inherits from BaseCaching"""

    def __init__(self):
        """ Initiliaze the BasicCache instance"""
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
