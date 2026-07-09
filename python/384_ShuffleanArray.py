#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 3:55 AM
# @Author  : huxiaoman
# @File    : 384_ShuffleanArray.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


import random


class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.original = list(nums)

    def reset(self):
        """
        :rtype: List[int]
        """
        return list(self.original)

    def shuffle(self):
        """
        :rtype: List[int]
        """
        result = list(self.original)
        random.shuffle(result)
        return result
