#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/4 12:30 PM
# @Author  : huxiaoman
# @File    : 76_MinimumWindowSubstring.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ''
        need = {}
        for ch in t:
            need[ch] = need.get(ch, 0) + 1
        missing = len(t)
        left = 0
        start = 0
        min_len = len(s) + 1
        for right, ch in enumerate(s):
            if ch in need:
                if need[ch] > 0:
                    missing -= 1
                need[ch] -= 1
            while missing == 0:
                if right - left + 1 < min_len:
                    start = left
                    min_len = right - left + 1
                left_ch = s[left]
                if left_ch in need:
                    need[left_ch] += 1
                    if need[left_ch] > 0:
                        missing += 1
                left += 1
        return '' if min_len == len(s) + 1 else s[start:start + min_len]
