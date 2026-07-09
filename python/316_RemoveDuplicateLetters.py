#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 10:25 PM
# @Author  : huxiaoman
# @File    : 316_RemoveDuplicateLetters.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


from collections import Counter


class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        counter = Counter(s)
        stack = []
        seen = set()
        for ch in s:
            counter[ch] -= 1
            if ch in seen:
                continue
            while stack and ch < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            stack.append(ch)
            seen.add(ch)
        return ''.join(stack)
