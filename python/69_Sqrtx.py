#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/4 11:20 AM
# @Author  : huxiaoman
# @File    : 69_Sqrtx.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x
        left, right = 1, x // 2
        while left <= right:
            mid = left + (right - left) // 2
            square = mid * mid
            if square == x:
                return mid
            if square < x:
                left = mid + 1
            else:
                right = mid - 1
        return right
