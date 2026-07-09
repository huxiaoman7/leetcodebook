#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/5 11:30 AM
# @Author  : huxiaoman
# @File    : 91_DecodeWays.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == '0':
            return 0
        prev2, prev1 = 1, 1
        for i in range(1, len(s)):
            cur = 0
            if s[i] != '0':
                cur += prev1
            two = int(s[i - 1:i + 1])
            if 10 <= two <= 26:
                cur += prev2
            prev2, prev1 = prev1, cur
        return prev1
