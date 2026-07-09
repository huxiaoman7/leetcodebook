#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/3 10:10 AM
# @Author  : huxiaoman
# @File    : 150_EvaluateReversePolishNotation.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for token in tokens:
            if token not in ['+', '-', '*', '/']:
                stack.append(int(token))
                continue
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            else:
                stack.append(int(float(a) / b))
        return stack[-1]
