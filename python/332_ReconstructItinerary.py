#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 11:45 PM
# @Author  : huxiaoman
# @File    : 332_ReconstructItinerary.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


from collections import defaultdict


class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        graph = defaultdict(list)
        for src, dst in sorted(tickets, reverse=True):
            graph[src].append(dst)
        route = []

        def visit(airport):
            while graph[airport]:
                visit(graph[airport].pop())
            route.append(airport)

        visit('JFK')
        return route[::-1]
