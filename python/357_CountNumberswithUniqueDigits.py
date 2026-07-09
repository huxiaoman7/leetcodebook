#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 1:50 AM
# @Author  : huxiaoman
# @File    : 357_CountNumberswithUniqueDigits.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        total = 10
        unique = 9
        available = 9
        for _ in range(2, min(n, 10) + 1):
            unique *= available
            total += unique
            available -= 1
        return total
