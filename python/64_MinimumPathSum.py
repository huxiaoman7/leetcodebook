#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/4 10:30 AM
# @Author  : huxiaoman
# @File    : 64_MinimumPathSum.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        dp = [0] * n
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[j] = grid[i][j]
                elif i == 0:
                    dp[j] = dp[j - 1] + grid[i][j]
                elif j == 0:
                    dp[j] = dp[j] + grid[i][j]
                else:
                    dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]
        return dp[-1]
