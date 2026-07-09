#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/6 12:20 PM
# @Author  : huxiaoman
# @File    : 115_DistinctSubsequences.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        dp = [0] * (len(t) + 1)
        dp[0] = 1
        for ch in s:
            for j in range(len(t) - 1, -1, -1):
                if ch == t[j]:
                    dp[j + 1] += dp[j]
        return dp[-1]
