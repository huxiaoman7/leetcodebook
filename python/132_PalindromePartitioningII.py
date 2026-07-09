#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/7 11:50 AM
# @Author  : huxiaoman
# @File    : 132_PalindromePartitioningII.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        cut = list(range(n))
        pal = [[False] * n for _ in range(n)]
        for i in range(n):
            min_cut = i
            for j in range(i + 1):
                if s[i] == s[j] and (i - j < 2 or pal[j + 1][i - 1]):
                    pal[j][i] = True
                    min_cut = 0 if j == 0 else min(min_cut, cut[j - 1] + 1)
            cut[i] = min_cut
        return cut[-1] if s else 0
