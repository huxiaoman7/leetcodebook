#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 11:10 AM
# @Author  : huxiaoman
# @File    : 168_ExcelSheetColumnTitle.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = []
        while n:
            n -= 1
            result.append(chr(ord('A') + n % 26))
            n //= 26
        return ''.join(reversed(result))
