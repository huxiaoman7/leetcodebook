#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/7 11:30 AM
# @Author  : huxiaoman
# @File    : 130_SurroundedRegions.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        m, n = len(board), len(board[0])

        def mark(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != 'O':
                return
            board[i][j] = '#'
            mark(i + 1, j)
            mark(i - 1, j)
            mark(i, j + 1)
            mark(i, j - 1)

        for i in range(m):
            mark(i, 0)
            mark(i, n - 1)
        for j in range(n):
            mark(0, j)
            mark(m - 1, j)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'
