#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 7:20 PM
# @Author  : huxiaoman
# @File    : 279_PerfectSquares.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] + [float('inf')] * n
        squares = [i * i for i in range(1, int(n ** 0.5) + 1)]
        for i in range(1, n + 1):
            for square in squares:
                if square > i:
                    break
                dp[i] = min(dp[i], dp[i - square] + 1)
        return dp[n]
