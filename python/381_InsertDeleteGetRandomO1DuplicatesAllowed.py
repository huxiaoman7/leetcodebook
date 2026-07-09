#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 3:40 AM
# @Author  : huxiaoman
# @File    : 381_InsertDeleteGetRandomO1DuplicatesAllowed.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


import random
from collections import defaultdict


class RandomizedCollection(object):

    def __init__(self):
        self.values = []
        self.indexes = defaultdict(set)

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        existed = bool(self.indexes[val])
        self.indexes[val].add(len(self.values))
        self.values.append(val)
        return not existed

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if not self.indexes[val]:
            return False
        remove_index = self.indexes[val].pop()
        last = self.values[-1]
        self.values[remove_index] = last
        self.indexes[last].add(remove_index)
        self.indexes[last].discard(len(self.values) - 1)
        self.values.pop()
        return True

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.values)
