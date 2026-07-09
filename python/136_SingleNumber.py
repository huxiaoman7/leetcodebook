#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/7 12:30 PM
# @Author  : huxiaoman
# @File    : 136_SingleNumber.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for num in nums:
            result ^= num
        return result
