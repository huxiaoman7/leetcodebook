#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 9:40 PM
# @Author  : huxiaoman
# @File    : 307_RangeSumQueryMutable.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums[:]
        self.tree = [0] * (len(nums) + 1)
        for i, num in enumerate(nums):
            self.add(i + 1, num)

    def update(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        delta = val - self.nums[index]
        self.nums[index] = val
        self.add(index + 1, delta)

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.prefix(right + 1) - self.prefix(left)

    def add(self, index, delta):
        while index < len(self.tree):
            self.tree[index] += delta
            index += index & -index

    def prefix(self, index):
        total = 0
        while index > 0:
            total += self.tree[index]
            index -= index & -index
        return total
