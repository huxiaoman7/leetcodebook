#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/3 11:20 AM
# @Author  : huxiaoman
# @File    : 53_MaximumSubarray.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur = nums[0]
        result = nums[0]
        for num in nums[1:]:
            cur = max(num, cur + num)
            result = max(result, cur)
        return result
