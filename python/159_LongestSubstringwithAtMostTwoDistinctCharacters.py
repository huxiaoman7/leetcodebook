#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/8 12:40 PM
# @Author  : huxiaoman
# @File    : 159_LongestSubstringwithAtMostTwoDistinctCharacters.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = {}
        left = 0
        result = 0
        for right, ch in enumerate(s):
            count[ch] = count.get(ch, 0) + 1
            while len(count) > 2:
                count[s[left]] -= 1
                if count[s[left]] == 0:
                    del count[s[left]]
                left += 1
            result = max(result, right - left + 1)
        return result
