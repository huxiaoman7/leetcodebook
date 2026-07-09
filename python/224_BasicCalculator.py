#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 3:00 PM
# @Author  : huxiaoman
# @File    : 224_BasicCalculator.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        number = 0
        sign = 1
        stack = []
        for ch in s:
            if ch.isdigit():
                number = number * 10 + int(ch)
            elif ch in '+-':
                result += sign * number
                number = 0
                sign = 1 if ch == '+' else -1
            elif ch == '(':
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif ch == ')':
                result += sign * number
                number = 0
                result *= stack.pop()
                result += stack.pop()
        return result + sign * number
