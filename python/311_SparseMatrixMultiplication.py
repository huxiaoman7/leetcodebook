#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 10:00 PM
# @Author  : huxiaoman
# @File    : 311_SparseMatrixMultiplication.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def multiply(self, mat1, mat2):
        """
        :type mat1: List[List[int]]
        :type mat2: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n, p = len(mat1), len(mat2), len(mat2[0])
        result = [[0] * p for _ in range(m)]
        for i in range(m):
            for k in range(n):
                if mat1[i][k]:
                    for j in range(p):
                        if mat2[k][j]:
                            result[i][j] += mat1[i][k] * mat2[k][j]
        return result
