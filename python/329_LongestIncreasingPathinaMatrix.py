#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 11:30 PM
# @Author  : huxiaoman
# @File    : 329_LongestIncreasingPathinaMatrix.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        memo = {}
        return max(self.dfs(matrix, i, j, memo) for i in range(len(matrix)) for j in range(len(matrix[0])))

    def dfs(self, matrix, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]
        best = 1
        for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and matrix[x][y] > matrix[i][j]:
                best = max(best, 1 + self.dfs(matrix, x, y, memo))
        memo[(i, j)] = best
        return best
