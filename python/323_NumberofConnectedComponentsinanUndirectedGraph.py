#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 11:00 PM
# @Author  : huxiaoman
# @File    : 323_NumberofConnectedComponentsinanUndirectedGraph.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        count = n
        for a, b in edges:
            root_a = find(a)
            root_b = find(b)
            if root_a != root_b:
                parent[root_a] = root_b
                count -= 1
        return count
