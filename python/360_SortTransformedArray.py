#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 2:05 AM
# @Author  : huxiaoman
# @File    : 360_SortTransformedArray.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        transformed = [self.f(num, a, b, c) for num in nums]
        return sorted(transformed)

    def f(self, x, a, b, c):
        return a * x * x + b * x + c
