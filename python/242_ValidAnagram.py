#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 4:20 PM
# @Author  : huxiaoman
# @File    : 242_ValidAnagram.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)
