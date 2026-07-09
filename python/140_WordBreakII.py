#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/7 1:10 PM
# @Author  : huxiaoman
# @File    : 140_WordBreakII.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        words = set(wordDict)
        memo = {}

        def dfs(start):
            if start in memo:
                return memo[start]
            if start == len(s):
                return ['']
            result = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in words:
                    for tail in dfs(end):
                        result.append(word if not tail else word + ' ' + tail)
            memo[start] = result
            return result

        return dfs(0)
