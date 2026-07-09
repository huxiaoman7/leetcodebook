#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 12:30 PM
# @Author  : huxiaoman
# @File    : 186_ReverseWordsinaStringII.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        self.reverse(s, 0, len(s) - 1)
        start = 0
        for i in range(len(s) + 1):
            if i == len(s) or s[i] == ' ':
                self.reverse(s, start, i - 1)
                start = i + 1

    def reverse(self, s, left, right):
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
