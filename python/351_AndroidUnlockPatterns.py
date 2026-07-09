#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 1:20 AM
# @Author  : huxiaoman
# @File    : 351_AndroidUnlockPatterns.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        skip = [[0] * 10 for _ in range(10)]
        skip[1][3] = skip[3][1] = 2
        skip[1][7] = skip[7][1] = 4
        skip[3][9] = skip[9][3] = 6
        skip[7][9] = skip[9][7] = 8
        skip[1][9] = skip[9][1] = skip[3][7] = skip[7][3] = 5
        skip[2][8] = skip[8][2] = skip[4][6] = skip[6][4] = 5
        visited = [False] * 10
        total = 0
        for length in range(m, n + 1):
            total += self.dfs(1, length - 1, visited, skip) * 4
            total += self.dfs(2, length - 1, visited, skip) * 4
            total += self.dfs(5, length - 1, visited, skip)
        return total

    def dfs(self, current, remain, visited, skip):
        if remain == 0:
            return 1
        visited[current] = True
        total = 0
        for nxt in range(1, 10):
            if not visited[nxt] and (skip[current][nxt] == 0 or visited[skip[current][nxt]]):
                total += self.dfs(nxt, remain - 1, visited, skip)
        visited[current] = False
        return total
