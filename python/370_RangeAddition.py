#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 2:45 AM
# @Author  : huxiaoman
# @File    : 370_RangeAddition.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):

    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        diff = [0] * (length + 1)
        for start, end, inc in updates:
            diff[start] += inc
            if end + 1 < length:
                diff[end + 1] -= inc
        result = []
        current = 0
        for i in range(length):
            current += diff[i]
            result.append(current)
        return result
