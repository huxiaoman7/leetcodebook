#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/8 11:20 AM
# @Author  : huxiaoman
# @File    : 149_MaxPointsonaLine.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


import math


class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points) <= 2:
            return len(points)
        result = 0
        for i in range(len(points)):
            slopes = {}
            duplicate = 1
            for j in range(i + 1, len(points)):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]
                if dx == 0 and dy == 0:
                    duplicate += 1
                    continue
                gcd = math.gcd(dx, dy)
                dx //= gcd
                dy //= gcd
                if dx < 0:
                    dx, dy = -dx, -dy
                elif dx == 0:
                    dy = 1
                elif dy == 0:
                    dx = 1
                slopes[(dx, dy)] = slopes.get((dx, dy), 0) + 1
            result = max(result, duplicate)
            for count in slopes.values():
                result = max(result, count + duplicate)
        return result
