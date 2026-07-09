#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/5 10:50 AM
# @Author  : huxiaoman
# @File    : 87_ScrambleString.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        memo = {}

        def dfs(a, b):
            if (a, b) in memo:
                return memo[(a, b)]
            if a == b:
                memo[(a, b)] = True
                return True
            if sorted(a) != sorted(b):
                memo[(a, b)] = False
                return False
            for i in range(1, len(a)):
                if dfs(a[:i], b[:i]) and dfs(a[i:], b[i:]):
                    memo[(a, b)] = True
                    return True
                if dfs(a[:i], b[-i:]) and dfs(a[i:], b[:-i]):
                    memo[(a, b)] = True
                    return True
            memo[(a, b)] = False
            return False

        return dfs(s1, s2)
