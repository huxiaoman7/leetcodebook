#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 1:05 AM
# @Author  : huxiaoman
# @File    : 348_DesignTicTacToe.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class TicTacToe(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.n = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.diag = 0
        self.anti = 0

    def move(self, row, col, player):
        """
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        value = 1 if player == 1 else -1
        self.rows[row] += value
        self.cols[col] += value
        if row == col:
            self.diag += value
        if row + col == self.n - 1:
            self.anti += value
        if self.n in [abs(self.rows[row]), abs(self.cols[col]), abs(self.diag), abs(self.anti)]:
            return player
        return 0
