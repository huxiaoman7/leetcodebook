#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 9:55 PM
# @Author  : huxiaoman
# @File    : 310_MinimumHeightTrees.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


from collections import defaultdict


class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n <= 1:
            return [0]
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

        leaves = [node for node in range(n) if len(graph[node]) == 1]
        remaining = n
        while remaining > 2:
            remaining -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves
        return leaves
