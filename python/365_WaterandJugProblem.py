#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 2:20 AM
# @Author  : huxiaoman
# @File    : 365_WaterandJugProblem.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


import math


class Solution(object):

    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        if z == 0:
            return True
        if x + y < z:
            return False
        return z % math.gcd(x, y) == 0
