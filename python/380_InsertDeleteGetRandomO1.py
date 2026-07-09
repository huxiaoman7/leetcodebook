#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 3:35 AM
# @Author  : huxiaoman
# @File    : 380_InsertDeleteGetRandomO1.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


import random


class RandomizedSet(object):

    def __init__(self):
        self.values = []
        self.index = {}

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.index:
            return False
        self.index[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.index:
            return False
        remove_index = self.index.pop(val)
        last = self.values.pop()
        if remove_index < len(self.values):
            self.values[remove_index] = last
            self.index[last] = remove_index
        return True

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.values)
