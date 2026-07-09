#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/4 11:30 AM
# @Author  : huxiaoman
# @File    : 70_ClimbingStairs.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a, b = 1, 1
        for _ in range(n):
            a, b = b, a + b
        return a
