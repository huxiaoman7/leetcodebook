#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/8 11:40 AM
# @Author  : huxiaoman
# @File    : 152_MaximumProductSubarray.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_cur = min_cur = result = nums[0]
        for num in nums[1:]:
            if num < 0:
                max_cur, min_cur = min_cur, max_cur
            max_cur = max(num, max_cur * num)
            min_cur = min(num, min_cur * num)
            result = max(result, max_cur)
        return result
