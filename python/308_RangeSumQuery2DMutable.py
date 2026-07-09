#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 9:45 PM
# @Author  : huxiaoman
# @File    : 308_RangeSumQuery2DMutable.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix = [row[:] for row in matrix]

    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: None
        """
        self.matrix[row][col] = val

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        total = 0
        for i in range(row1, row2 + 1):
            total += sum(self.matrix[i][col1:col2 + 1])
        return total
