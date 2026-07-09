#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 3:10 AM
# @Author  : huxiaoman
# @File    : 375_GuessNumberHigherorLowerII.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):

    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [[0] * (n + 2) for _ in range(n + 2)]
        for length in range(2, n + 1):
            for start in range(1, n - length + 2):
                end = start + length - 1
                dp[start][end] = min(
                    pivot + max(dp[start][pivot - 1], dp[pivot + 1][end])
                    for pivot in range(start, end + 1)
                )
        return dp[1][n]
