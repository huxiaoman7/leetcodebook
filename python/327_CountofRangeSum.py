#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 11:20 PM
# @Author  : huxiaoman
# @File    : 327_CountofRangeSum.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


import bisect


class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        prefix = 0
        prefixes = [0]
        count = 0
        for num in nums:
            prefix += num
            left = bisect.bisect_left(prefixes, prefix - upper)
            right = bisect.bisect_right(prefixes, prefix - lower)
            count += right - left
            bisect.insort(prefixes, prefix)
        return count
