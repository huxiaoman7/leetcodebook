#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/3 12:20 PM
# @Author  : huxiaoman
# @File    : 59_SpiralMatrixII.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0] * n for _ in range(n)]
        top, bottom = 0, n - 1
        left, right = 0, n - 1
        num = 1
        while top <= bottom and left <= right:
            for j in range(left, right + 1):
                matrix[top][j] = num
                num += 1
            top += 1
            for i in range(top, bottom + 1):
                matrix[i][right] = num
                num += 1
            right -= 1
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    matrix[bottom][j] = num
                    num += 1
                bottom -= 1
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    matrix[i][left] = num
                    num += 1
                left += 1
        return matrix
