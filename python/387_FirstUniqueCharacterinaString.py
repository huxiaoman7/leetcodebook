#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 4:10 AM
# @Author  : huxiaoman
# @File    : 387_FirstUniqueCharacterinaString.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


from collections import Counter


class Solution(object):

    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        counts = Counter(s)
        for i, ch in enumerate(s):
            if counts[ch] == 1:
                return i
        return -1
