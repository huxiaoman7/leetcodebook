#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 12:15 AM
# @Author  : huxiaoman
# @File    : 338_CountingBits.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = [0] * (n + 1)
        for i in range(1, n + 1):
            result[i] = result[i >> 1] + (i & 1)
        return result
