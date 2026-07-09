#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 12:20 PM
# @Author  : huxiaoman
# @File    : 179_LargestNumber.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


from functools import cmp_to_key


class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = [str(num) for num in nums]

        def compare(a, b):
            if a + b > b + a:
                return -1
            if a + b < b + a:
                return 1
            return 0

        result = ''.join(sorted(nums, key=cmp_to_key(compare)))
        return '0' if result[0] == '0' else result
