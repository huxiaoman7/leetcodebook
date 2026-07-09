#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 3:15 PM
# @Author  : huxiaoman
# @File    : 227_BasicCalculatorII.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        number = 0
        sign = '+'
        for i, ch in enumerate(s):
            if ch.isdigit():
                number = number * 10 + int(ch)
            if (not ch.isdigit() and ch != ' ') or i == len(s) - 1:
                if sign == '+':
                    stack.append(number)
                elif sign == '-':
                    stack.append(-number)
                elif sign == '*':
                    stack.append(stack.pop() * number)
                elif sign == '/':
                    prev = stack.pop()
                    stack.append(int(float(prev) / number))
                sign = ch
                number = 0
        return sum(stack)
