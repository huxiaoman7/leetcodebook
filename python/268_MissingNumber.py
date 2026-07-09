#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 6:25 PM
# @Author  : huxiaoman
# @File    : 268_MissingNumber.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = len(nums)
        for i, num in enumerate(nums):
            result ^= i ^ num
        return result
