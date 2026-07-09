#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 9:10 PM
# @Author  : huxiaoman
# @File    : 301_RemoveInvalidParentheses.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        level = {s}
        while True:
            valid = [item for item in level if self.is_valid(item)]
            if valid:
                return valid
            next_level = set()
            for item in level:
                for i, ch in enumerate(item):
                    if ch in '()':
                        next_level.add(item[:i] + item[i + 1:])
            level = next_level

    def is_valid(self, s):
        count = 0
        for ch in s:
            if ch == '(':
                count += 1
            elif ch == ')':
                count -= 1
                if count < 0:
                    return False
        return count == 0
