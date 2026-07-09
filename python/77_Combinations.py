#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/4 12:40 PM
# @Author  : huxiaoman
# @File    : 77_Combinations.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []

        def dfs(start, path):
            if len(path) == k:
                result.append(path[:])
                return
            for num in range(start, n + 1):
                path.append(num)
                dfs(num + 1, path)
                path.pop()

        dfs(1, [])
        return result
