#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 1:45 AM
# @Author  : huxiaoman
# @File    : 356_LineReflection.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        point_set = set(map(tuple, points))
        min_x = min(x for x, _ in points)
        max_x = max(x for x, _ in points)
        total = min_x + max_x
        return all((total - x, y) in point_set for x, y in points)
