#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/4 11:00 AM
# @Author  : huxiaoman
# @File    : 67_AddBinary.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        result = []
        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += ord(a[i]) - ord('0')
                i -= 1
            if j >= 0:
                total += ord(b[j]) - ord('0')
                j -= 1
            result.append(str(total % 2))
            carry = total // 2
        return ''.join(reversed(result))
