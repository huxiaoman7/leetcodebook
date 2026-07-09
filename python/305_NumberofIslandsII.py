#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 9:30 PM
# @Author  : huxiaoman
# @File    : 305_NumberofIslandsII.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        parent = {}
        count = 0
        result = []

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for i, j in positions:
            if (i, j) in parent:
                result.append(count)
                continue
            parent[(i, j)] = (i, j)
            count += 1
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if (x, y) in parent:
                    root1 = find((i, j))
                    root2 = find((x, y))
                    if root1 != root2:
                        parent[root1] = root2
                        count -= 1
            result.append(count)
        return result
