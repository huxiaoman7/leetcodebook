#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/4 10:40 AM
# @Author  : huxiaoman
# @File    : 65_ValidNumber.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        if not s:
            return False

        seen_digit = False
        seen_dot = False
        seen_exp = False
        digit_after_exp = True

        for i, ch in enumerate(s):
            if ch.isdigit():
                seen_digit = True
                if seen_exp:
                    digit_after_exp = True
            elif ch in ['+', '-']:
                if i != 0 and s[i - 1] not in ['e', 'E']:
                    return False
            elif ch == '.':
                if seen_dot or seen_exp:
                    return False
                seen_dot = True
            elif ch in ['e', 'E']:
                if seen_exp or not seen_digit:
                    return False
                seen_exp = True
                digit_after_exp = False
            else:
                return False
        return seen_digit and digit_after_exp
