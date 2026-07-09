#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 4:30 AM
# @Author  : huxiaoman
# @File    : 391_PerfectRectangle.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):

    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        area = 0
        corners = set()
        min_x = min_y = float('inf')
        max_x = max_y = -float('inf')
        for x1, y1, x2, y2 in rectangles:
            min_x, min_y = min(min_x, x1), min(min_y, y1)
            max_x, max_y = max(max_x, x2), max(max_y, y2)
            area += (x2 - x1) * (y2 - y1)
            for corner in ((x1, y1), (x1, y2), (x2, y1), (x2, y2)):
                if corner in corners:
                    corners.remove(corner)
                else:
                    corners.add(corner)
        expected = (max_x - min_x) * (max_y - min_y)
        return area == expected and corners == {
            (min_x, min_y), (min_x, max_y), (max_x, min_y), (max_x, max_y)
        }
