#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/5 10:30 AM
# @Author  : huxiaoman
# @File    : 85_MaximalRectangle.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        n = len(matrix[0])
        heights = [0] * n
        result = 0
        for row in matrix:
            for i in range(n):
                heights[i] = heights[i] + 1 if row[i] == '1' else 0
            result = max(result, self.largestRectangleArea(heights))
        return result

    def largestRectangleArea(self, heights):
        stack = []
        result = 0
        arr = heights + [0]
        for i, h in enumerate(arr):
            while stack and arr[stack[-1]] > h:
                height = arr[stack.pop()]
                left = stack[-1] if stack else -1
                result = max(result, height * (i - left - 1))
            stack.append(i)
        return result
