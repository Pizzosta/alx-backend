#!/usr/bin/python3
""" LRUCache module
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache class that inherits from BaseCaching"""

    def __init__(self):
        """ Initiliaze the LRUCache instance"""
        super().__init__()
        self.lru_queue = []

    def put(self, key, item):
        """ Add an item in the cache"""
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                lru_key = self.lru_queue.pop(0)
                print("DISCARD:", lru_key)
                del self.cache_data[lru_key]
            self.cache_data[key] = item
            self.lru_queue.append(key)

    def get(self, key):
        """ Get an item by key"""
        if key is not None and key in self.cache_data:
            self.lru_queue.remove(key)
            self.lru_queue.append(key)
            return self.cache_data[key]
        return None
