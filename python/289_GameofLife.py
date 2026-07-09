#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 8:10 PM
# @Author  : huxiaoman
# @File    : 289_GameofLife.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                lives = 0
                for x in range(max(0, i - 1), min(m, i + 2)):
                    for y in range(max(0, j - 1), min(n, j + 2)):
                        lives += board[x][y] & 1
                if board[i][j] and lives in [3, 4]:
                    board[i][j] |= 2
                if not board[i][j] and lives == 3:
                    board[i][j] |= 2
        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1
