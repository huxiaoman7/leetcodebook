#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 9:15 PM
# @Author  : huxiaoman
# @File    : 302_SmallestRectangleEnclosingBlackPixels.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        top = bottom = x
        left = right = y
        for i in range(len(image)):
            for j in range(len(image[0])):
                if image[i][j] == '1':
                    top = min(top, i)
                    bottom = max(bottom, i)
                    left = min(left, j)
                    right = max(right, j)
        return (bottom - top + 1) * (right - left + 1)
