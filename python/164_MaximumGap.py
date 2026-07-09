#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 10:30 AM
# @Author  : huxiaoman
# @File    : 164_MaximumGap.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        nums.sort()
        result = 0
        for i in range(1, len(nums)):
            result = max(result, nums[i] - nums[i - 1])
        return result
