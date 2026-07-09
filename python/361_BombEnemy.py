#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 2:00 AM
# @Author  : huxiaoman
# @File    : 361_BombEnemy.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):

    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        result = 0
        row_hits = 0
        col_hits = [0] * n
        for i in range(m):
            for j in range(n):
                if j == 0 or grid[i][j - 1] == 'W':
                    row_hits = 0
                    k = j
                    while k < n and grid[i][k] != 'W':
                        row_hits += grid[i][k] == 'E'
                        k += 1
                if i == 0 or grid[i - 1][j] == 'W':
                    col_hits[j] = 0
                    k = i
                    while k < m and grid[k][j] != 'W':
                        col_hits[j] += grid[k][j] == 'E'
                        k += 1
                if grid[i][j] == '0':
                    result = max(result, row_hits + col_hits[j])
        return result
