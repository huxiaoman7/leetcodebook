#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/3 11:10 AM
# @Author  : huxiaoman
# @File    : 52_NQueensII.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.count = 0
        cols = set()
        diag1 = set()
        diag2 = set()

        def dfs(row):
            if row == n:
                self.count += 1
                return
            for col in range(n):
                if col in cols or row + col in diag1 or row - col in diag2:
                    continue
                cols.add(col)
                diag1.add(row + col)
                diag2.add(row - col)
                dfs(row + 1)
                cols.remove(col)
                diag1.remove(row + col)
                diag2.remove(row - col)

        dfs(0)
        return self.count
