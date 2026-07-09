#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/4 1:00 PM
# @Author  : huxiaoman
# @File    : 79_WordSearch.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not board[0]:
            return False
        m, n = len(board), len(board[0])

        def dfs(i, j, index):
            if index == len(word):
                return True
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[index]:
                return False
            temp = board[i][j]
            board[i][j] = '#'
            found = (dfs(i + 1, j, index + 1) or
                     dfs(i - 1, j, index + 1) or
                     dfs(i, j + 1, index + 1) or
                     dfs(i, j - 1, index + 1))
            board[i][j] = temp
            return found

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False
