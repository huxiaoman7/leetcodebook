#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 12:50 PM
# @Author  : huxiaoman
# @File    : 190_ReverseBits.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        for _ in range(32):
            result = (result << 1) | (n & 1)
            n >>= 1
        return result
