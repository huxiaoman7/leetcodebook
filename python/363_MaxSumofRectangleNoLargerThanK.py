#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 2:10 AM
# @Author  : huxiaoman
# @File    : 363_MaxSumofRectangleNoLargerThanK.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


import bisect


class Solution(object):

    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        result = -float('inf')
        for left in range(n):
            rows = [0] * m
            for right in range(left, n):
                for i in range(m):
                    rows[i] += matrix[i][right]
                prefix = 0
                prefixes = [0]
                for value in rows:
                    prefix += value
                    index = bisect.bisect_left(prefixes, prefix - k)
                    if index < len(prefixes):
                        result = max(result, prefix - prefixes[index])
                    bisect.insort(prefixes, prefix)
        return result
