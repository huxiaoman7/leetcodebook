#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 11:10 PM
# @Author  : huxiaoman
# @File    : 325_MaximumSizeSubarraySumEqualsk.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        first = {0: -1}
        total = 0
        result = 0
        for i, num in enumerate(nums):
            total += num
            if total - k in first:
                result = max(result, i - first[total - k])
            if total not in first:
                first[total] = i
        return result
