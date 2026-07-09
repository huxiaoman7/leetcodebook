#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 5:10 AM
# @Author  : huxiaoman
# @File    : 399_EvaluateDivision.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


from collections import defaultdict


class Solution(object):

    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = defaultdict(list)
        for (a, b), value in zip(equations, values):
            graph[a].append((b, value))
            graph[b].append((a, 1.0 / value))

        def search(start, end, seen):
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0
            seen.add(start)
            for neighbor, value in graph[start]:
                if neighbor in seen:
                    continue
                result = search(neighbor, end, seen)
                if result != -1.0:
                    return value * result
            return -1.0

        return [search(start, end, set()) for start, end in queries]
