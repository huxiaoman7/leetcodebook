#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 12:40 AM
# @Author  : huxiaoman
# @File    : 343_IntegerBreak.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 3:
            return n - 1
        result = 1
        while n > 4:
            result *= 3
            n -= 3
        return result * n
