#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/2 11:12 AM
# @Author  : huxiaoman
# @File    : 133_CloneGraph.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com

# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []



class Solution:
    # BFS
    def cloneGraph1(self, node):
        if not node:
            return
        # node = UndirectedGraphNode()
        nodeCopy = UndirectedGraphNode(node.label)
        dic = {node: nodeCopy}
        queue = collections.deque([node])
        while queue:
            node = queue.popleft()
            for neighbor in node.neighbors:
                if neighbor not in dic: # neighbor is not visited
                    neighborCopy = UndirectedGraphNode(neighbor.label)
                    dic[neighbor] = neighborCopy
                       dic[node].neighbors.append(neighborCopy)
                    queue.append(neighbor)
                else:
                    dic[node].neighbors.append(dic[neighbor])
        return nodeCopy

    # DFS iteratively
    def cloneGraph2(self, node):
        if not node:
            return
        nodeCopy = UndirectedGraphNode(node.label)
        dic = {node: nodeCopy}
        stack = [node]
        while stack:
            node = stack.pop()
            for neighbor in node.neighbors:
                if neighbor not in dic:
                    neighborCopy = UndirectedGraphNode(neighbor.label)
                    dic[neighbor] = neighborCopy
                    dic[node].neighbors.append(neighborCopy)
                    stack.append(neighbor)
                else:
                    dic[node].neighbors.append(dic[neighbor])
        return nodeCopy

    # DFS recursively
    def cloneGraph(self, node):
        if not node:
            return
        nodeCopy = UndirectedGraphNode(node.label)
        dic = {node: nodeCopy}
        self.dfs(node, dic)
        return nodeCopy

    def dfs(self, node, dic):
        for neighbor in node.neighbors:
            if neighbor not in dic:
                neighborCopy = UndirectedGraphNode(neighbor.label)
                dic[neighbor] = neighborCopy
                dic[node].neighbors.append(neighborCopy)
                self.dfs(neighbor, dic)
            else:
                dic[node].neighbors.append(dic[neighbor])

if __name__ == '__main__':
    s = Solution()
    print s.cloneGraph1({"$id":"1","neighbors":[{"$id":"2","neighbors":[{"$ref":"1"},{"$id":"3","neighbors":[{"$ref":"2"},{"$id":"4","neighbors":[{"$ref":"3"},{"$ref":"1"}],"val":4}],"val":3}],"val":2},{"$ref":"4"}],"val":1})