#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 1:25 AM
# @Author  : huxiaoman
# @File    : 352_DataStreamasDisjointIntervals.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class SummaryRanges(object):

    def __init__(self):
        self.values = set()

    def addNum(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.values.add(val)

    def getIntervals(self):
        """
        :rtype: List[List[int]]
        """
        result = []
        for value in sorted(self.values):
            if not result or value > result[-1][1] + 1:
                result.append([value, value])
            else:
                result[-1][1] = value
        return result
