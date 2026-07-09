#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/3 12:10 PM
# @Author  : huxiaoman
# @File    : 58_LengthofLastWord.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.strip().split()
        return len(words[-1]) if words else 0
