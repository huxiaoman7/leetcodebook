#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 4:35 AM
# @Author  : huxiaoman
# @File    : 392_IsSubsequence.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):

    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        index = 0
        for ch in t:
            if index < len(s) and s[index] == ch:
                index += 1
        return index == len(s)
