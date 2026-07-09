#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 4:50 AM
# @Author  : huxiaoman
# @File    : 395_LongestSubstringwithAtLeastKRepeatingCharacters.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


from collections import Counter


class Solution(object):

    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s) < k:
            return 0
        counts = Counter(s)
        for ch, count in counts.items():
            if count < k:
                return max(self.longestSubstring(part, k) for part in s.split(ch))
        return len(s)
