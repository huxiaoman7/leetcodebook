#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 3:25 AM
# @Author  : huxiaoman
# @File    : 378_KthSmallestElementinaSortedMatrix.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):

    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)
        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            mid = (left + right) // 2
            count = 0
            row, col = n - 1, 0
            while row >= 0 and col < n:
                if matrix[row][col] <= mid:
                    count += row + 1
                    col += 1
                else:
                    row -= 1
            if count < k:
                left = mid + 1
            else:
                right = mid
        return left
