#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 5:15 AM
# @Author  : huxiaoman
# @File    : 400_NthDigit.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):

    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        digit = 1
        start = 1
        count = 9
        while n > digit * count:
            n -= digit * count
            digit += 1
            start *= 10
            count *= 10
        number = start + (n - 1) // digit
        return int(str(number)[(n - 1) % digit])
