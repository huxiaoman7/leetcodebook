#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/4 12:10 PM
# @Author  : huxiaoman
# @File    : 74_Searcha2DMatrix.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        while left <= right:
            mid = left + (right - left) // 2
            value = matrix[mid // n][mid % n]
            if value == target:
                return True
            if value < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
