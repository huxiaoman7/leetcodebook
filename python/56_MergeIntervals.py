#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/3 11:50 AM
# @Author  : huxiaoman
# @File    : 56_MergeIntervals.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]
        for interval in intervals[1:]:
            if interval[0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], interval[1])
            else:
                result.append(interval)
        return result
