#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 5:30 PM
# @Author  : huxiaoman
# @File    : 256_PaintHouse.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:
            return 0
        red = blue = green = 0
        for r, b, g in costs:
            red, blue, green = r + min(blue, green), b + min(red, green), g + min(red, blue)
        return min(red, blue, green)
