#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 5:50 PM
# @Author  : huxiaoman
# @File    : 260_SingleNumberIII.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = 0
        for num in nums:
            xor ^= num
        diff = xor & -xor
        a = 0
        b = 0
        for num in nums:
            if num & diff:
                a ^= num
            else:
                b ^= num
        return [a, b]
