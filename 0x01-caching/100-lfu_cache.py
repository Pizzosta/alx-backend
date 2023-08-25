#!/usr/bin/env python3
""" BaseCaching module
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache defines a LFU caching system
    """

    def __init__(self):
        """
        Initialize the class with the parent's init method
        """
        super().__init__()
        self.cache_usage = {}

    def put(self, key, item):
        """
        Cache a key-value pair
        """
        if key is None or item is None:
            pass
        else:
            length = len(self.cache_data)
            if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                lfu = min(self.cache_usage.values())
                lfu_keys = [k for k, v in self.cache_usage.items() if v == lfu]
                discard = min(lfu_keys, key=lambda k: self.cache_usage[k])
                print("DISCARD: {}".format(discard))
                del self.cache_data[discard]
                del self.cache_usage[discard]

            # Update usage frequency
            if key in self.cache_usage:
                self.cache_usage[key] += 1
            else:
                self.cache_usage[key] = 1

            self.cache_data[key] = item

    def get(self, key):
        """
        Return the value linked to a given key, or None
        """
        if key is not None and key in self.cache_data.keys():
            self.cache_usage[key] += 1
            return self.cache_data[key]
        return None
