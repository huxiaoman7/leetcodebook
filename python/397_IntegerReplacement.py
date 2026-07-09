#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 5:00 AM
# @Author  : huxiaoman
# @File    : 397_IntegerReplacement.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):

    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        steps = 0
        while n != 1:
            if n % 2 == 0:
                n //= 2
            elif n == 3 or n % 4 == 1:
                n -= 1
            else:
                n += 1
            steps += 1
        return steps
