#!/usr/bin/python3
""" MRUCache module
"""

from base_caching import BaseCaching

class MRUCache(BaseCaching):
    """ MRUCache class that inherits from BaseCaching """

    def __init__(self):
        """ Initialize the MRUCache instance """
        super().__init__()
        self.mru_queue = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                mru_key = self.mru_queue.pop()
                print("DISCARD:", mru_key)
                del self.cache_data[mru_key]
            self.cache_data[key] = item
            self.mru_queue.append(key)

    def get(self, key):
        """ Get an item by key """
        if key is not None and key in self.cache_data:
            self.mru_queue.remove(key)
            self.mru_queue.append(key)
            return self.cache_data[key]
        return None
