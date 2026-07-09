#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 12:25 AM
# @Author  : huxiaoman
# @File    : 340_LongestSubstringwithAtMostKDistinctCharacters.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


from collections import defaultdict


class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if k == 0:
            return 0
        counts = defaultdict(int)
        left = 0
        result = 0
        for right, ch in enumerate(s):
            counts[ch] += 1
            while len(counts) > k:
                counts[s[left]] -= 1
                if counts[s[left]] == 0:
                    del counts[s[left]]
                left += 1
            result = max(result, right - left + 1)
        return result
