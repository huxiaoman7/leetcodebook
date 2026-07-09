#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 9:20 PM
# @Author  : huxiaoman
# @File    : 303_RangeSumQueryImmutable.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.prefix = [0]
        for num in nums:
            self.prefix.append(self.prefix[-1] + num)

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.prefix[right + 1] - self.prefix[left]
