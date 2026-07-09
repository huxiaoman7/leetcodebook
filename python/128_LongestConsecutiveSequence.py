#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/7 11:10 AM
# @Author  : huxiaoman
# @File    : 128_LongestConsecutiveSequence.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        result = 0
        for num in nums:
            if num - 1 not in nums:
                cur = num
                length = 1
                while cur + 1 in nums:
                    cur += 1
                    length += 1
                result = max(result, length)
        return result
