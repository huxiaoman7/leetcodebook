#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 12:55 PM
# @Author  : huxiaoman
# @File    : 191_Numberof1Bits.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count
