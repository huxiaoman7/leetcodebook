#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 2:30 PM
# @Author  : huxiaoman
# @File    : 218_TheSkylineProblem.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


import heapq


class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        events = []
        for left, right, height in buildings:
            events.append((left, -height, right))
            events.append((right, 0, 0))
        events.sort()

        result = []
        heap = [(0, float('inf'))]
        for x, neg_height, right in events:
            while heap[0][1] <= x:
                heapq.heappop(heap)
            if neg_height:
                heapq.heappush(heap, (neg_height, right))
            height = -heap[0][0]
            if not result or result[-1][1] != height:
                result.append([x, height])
        return result
