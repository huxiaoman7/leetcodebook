#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 4:20 AM
# @Author  : huxiaoman
# @File    : 389_FindtheDifference.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):

    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        code = 0
        for ch in s + t:
            code ^= ord(ch)
        return chr(code)
