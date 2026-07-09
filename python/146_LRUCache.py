#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/8 10:50 AM
# @Author  : huxiaoman
# @File    : 146_LRUCache.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


from collections import OrderedDict


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        value = self.cache.pop(key)
        self.cache[key] = value
        return value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) == self.capacity:
            self.cache.popitem(last=False)
        self.cache[key] = value
