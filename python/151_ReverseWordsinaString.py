#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/8 11:30 AM
# @Author  : huxiaoman
# @File    : 151_ReverseWordsinaString.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(reversed(s.split()))
