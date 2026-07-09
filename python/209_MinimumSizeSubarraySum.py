#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 1:45 PM
# @Author  : huxiaoman
# @File    : 209_MinimumSizeSubarraySum.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        total = 0
        result = len(nums) + 1
        for right, num in enumerate(nums):
            total += num
            while total >= s:
                result = min(result, right - left + 1)
                total -= nums[left]
                left += 1
        return 0 if result == len(nums) + 1 else result
