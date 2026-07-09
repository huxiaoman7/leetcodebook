#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 2:00 PM
# @Author  : huxiaoman
# @File    : 212_WordSearchII.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if not board or not board[0]:
            return []

        root = {}
        for word in words:
            node = root
            for ch in word:
                node = node.setdefault(ch, {})
            node['#'] = word

        result = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, i, j, root, result)
        return result

    def dfs(self, board, i, j, node, result):
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
            return
        ch = board[i][j]
        if ch not in node:
            return

        nxt = node[ch]
        word = nxt.pop('#', None)
        if word:
            result.append(word)

        board[i][j] = '*'
        self.dfs(board, i + 1, j, nxt, result)
        self.dfs(board, i - 1, j, nxt, result)
        self.dfs(board, i, j + 1, nxt, result)
        self.dfs(board, i, j - 1, nxt, result)
        board[i][j] = ch
