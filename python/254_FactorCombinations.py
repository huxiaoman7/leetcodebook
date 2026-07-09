#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 5:20 PM
# @Author  : huxiaoman
# @File    : 254_FactorCombinations.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        result = []
        self.backtrack(n, 2, [], result)
        return result

    def backtrack(self, n, start, path, result):
        factor = start
        while factor * factor <= n:
            if n % factor == 0:
                result.append(path + [factor, n // factor])
                self.backtrack(n // factor, factor, path + [factor], result)
            factor += 1
