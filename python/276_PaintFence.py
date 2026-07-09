#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 7:05 PM
# @Author  : huxiaoman
# @File    : 276_PaintFence.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return k
        same = k
        diff = k * (k - 1)
        for _ in range(3, n + 1):
            same, diff = diff, (same + diff) * (k - 1)
        return same + diff
