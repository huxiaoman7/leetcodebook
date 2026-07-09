#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/3 10:00 AM
# @Author  : huxiaoman
# @File    : 84_LargestRectangleinHistogram.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        result = 0
        heights.append(0)
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                left = stack[-1] if stack else -1
                result = max(result, height * (i - left - 1))
            stack.append(i)
        heights.pop()
        return result
