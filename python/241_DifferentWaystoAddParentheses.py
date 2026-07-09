#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 4:15 PM
# @Author  : huxiaoman
# @File    : 241_DifferentWaystoAddParentheses.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        memo = {}
        return self.compute(expression, memo)

    def compute(self, expression, memo):
        if expression in memo:
            return memo[expression]
        result = []
        for i, ch in enumerate(expression):
            if ch in '+-*':
                for left in self.compute(expression[:i], memo):
                    for right in self.compute(expression[i + 1:], memo):
                        if ch == '+':
                            result.append(left + right)
                        elif ch == '-':
                            result.append(left - right)
                        else:
                            result.append(left * right)
        if not result:
            result.append(int(expression))
        memo[expression] = result
        return result
