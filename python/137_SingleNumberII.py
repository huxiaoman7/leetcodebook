#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/7 12:40 PM
# @Author  : huxiaoman
# @File    : 137_SingleNumberII.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ones = 0
        twos = 0
        for num in nums:
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones
        return ones
