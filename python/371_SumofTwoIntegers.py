#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 2:50 AM
# @Author  : huxiaoman
# @File    : 371_SumofTwoIntegers.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):

    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        mask = 0xffffffff
        max_int = 0x7fffffff
        while b:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        return a if a <= max_int else ~(a ^ mask)
