#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 3:40 PM
# @Author  : huxiaoman
# @File    : 233_NumberofDigitOne.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        factor = 1
        while factor <= n:
            lower = n - (n // factor) * factor
            current = (n // factor) % 10
            higher = n // (factor * 10)
            if current == 0:
                count += higher * factor
            elif current == 1:
                count += higher * factor + lower + 1
            else:
                count += (higher + 1) * factor
            factor *= 10
        return count
