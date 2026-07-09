#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 10:20 PM
# @Author  : huxiaoman
# @File    : 315_CountofSmallerNumbersAfterSelf.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


import bisect


class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sorted_nums = []
        result = []
        for num in reversed(nums):
            index = bisect.bisect_left(sorted_nums, num)
            result.append(index)
            bisect.insort(sorted_nums, num)
        return result[::-1]
