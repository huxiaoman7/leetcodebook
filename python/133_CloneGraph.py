#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/2 11:12 AM
# @Author  : huxiaoman
# @File    : 133_CloneGraph.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class UndirectedGraphNode(object):
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        if not node:
            return None
        clone = UndirectedGraphNode(node.label)
        copies = {node: clone}
        queue = [node]
        for cur in queue:
            for neighbor in cur.neighbors:
                if neighbor not in copies:
                    copies[neighbor] = UndirectedGraphNode(neighbor.label)
                    queue.append(neighbor)
                copies[cur].neighbors.append(copies[neighbor])
        return clone
