#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 6:30 PM
# @Author  : huxiaoman
# @File    : 269_AlienDictionary.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


from collections import defaultdict, deque


class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        graph = {ch: set() for word in words for ch in word}
        indegree = {ch: 0 for ch in graph}

        for first, second in zip(words, words[1:]):
            if len(first) > len(second) and first.startswith(second):
                return ''
            for a, b in zip(first, second):
                if a != b:
                    if b not in graph[a]:
                        graph[a].add(b)
                        indegree[b] += 1
                    break

        queue = deque([ch for ch in indegree if indegree[ch] == 0])
        order = []
        while queue:
            ch = queue.popleft()
            order.append(ch)
            for nxt in graph[ch]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)
        return ''.join(order) if len(order) == len(graph) else ''
