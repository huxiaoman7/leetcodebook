#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/6 12:50 PM
# @Author  : huxiaoman
# @File    : 118_PascalsTriangle.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        for i in range(numRows):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = result[i - 1][j - 1] + result[i - 1][j]
            result.append(row)
        return result
