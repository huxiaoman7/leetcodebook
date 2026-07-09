#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/3 11:00 AM
# @Author  : huxiaoman
# @File    : 51_NQueens.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        result = []
        board = []
        cols = set()
        diag1 = set()
        diag2 = set()

        def dfs(row):
            if row == n:
                result.append(board[:])
                return
            for col in range(n):
                if col in cols or row + col in diag1 or row - col in diag2:
                    continue
                cols.add(col)
                diag1.add(row + col)
                diag2.add(row - col)
                board.append('.' * col + 'Q' + '.' * (n - col - 1))
                dfs(row + 1)
                board.pop()
                cols.remove(col)
                diag1.remove(row + col)
                diag2.remove(row - col)

        dfs(0)
        return result
