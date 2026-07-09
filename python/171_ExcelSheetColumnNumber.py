#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 11:40 AM
# @Author  : huxiaoman
# @File    : 171_ExcelSheetColumnNumber.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        for ch in s:
            result = result * 26 + ord(ch) - ord('A') + 1
        return result
