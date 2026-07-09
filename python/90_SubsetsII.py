#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/5 11:20 AM
# @Author  : huxiaoman
# @File    : 90_SubsetsII.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = [[]]
        start = 0
        for i, num in enumerate(nums):
            size = len(result)
            begin = start if i > 0 and nums[i] == nums[i - 1] else 0
            for j in range(begin, size):
                result.append(result[j] + [num])
            start = size
        return result
