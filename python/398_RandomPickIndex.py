#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 5:05 AM
# @Author  : huxiaoman
# @File    : 398_RandomPickIndex.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


import random
from collections import defaultdict


class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.indexes = defaultdict(list)
        for i, num in enumerate(nums):
            self.indexes[num].append(i)

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        return random.choice(self.indexes[target])
