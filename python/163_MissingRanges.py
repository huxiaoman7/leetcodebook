#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 10:20 AM
# @Author  : huxiaoman
# @File    : 163_MissingRanges.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        result = []
        prev = lower - 1
        for i in range(len(nums) + 1):
            cur = nums[i] if i < len(nums) else upper + 1
            if cur - prev >= 2:
                result.append(self.formatRange(prev + 1, cur - 1))
            prev = cur
        return result

    def formatRange(self, start, end):
        return str(start) if start == end else str(start) + '->' + str(end)
