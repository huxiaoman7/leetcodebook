#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 6:15 PM
# @Author  : huxiaoman
# @File    : 266_PalindromePermutation.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


from collections import Counter


class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return sum(count % 2 for count in Counter(s).values()) <= 1
