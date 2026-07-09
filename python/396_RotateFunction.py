#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 4:55 AM
# @Author  : huxiaoman
# @File    : 396_RotateFunction.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):

    def maxRotateFunction(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        total = sum(nums)
        current = sum(i * num for i, num in enumerate(nums))
        result = current
        for i in range(n - 1, 0, -1):
            current += total - n * nums[i]
            result = max(result, current)
        return result
