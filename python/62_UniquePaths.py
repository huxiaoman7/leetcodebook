#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/4 10:10 AM
# @Author  : huxiaoman
# @File    : 62_UniquePaths.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [1] * n
        for _ in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]
        return dp[-1]
