#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/4 12:50 PM
# @Author  : huxiaoman
# @File    : 78_Subsets.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        for num in nums:
            result += [item + [num] for item in result]
        return result
