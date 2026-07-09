#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 4:45 AM
# @Author  : huxiaoman
# @File    : 394_DecodeString.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):

    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        current = ''
        count = 0
        for ch in s:
            if ch.isdigit():
                count = count * 10 + int(ch)
            elif ch == '[':
                stack.append((current, count))
                current = ''
                count = 0
            elif ch == ']':
                previous, repeat = stack.pop()
                current = previous + current * repeat
            else:
                current += ch
        return current
