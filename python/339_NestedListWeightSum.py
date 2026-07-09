#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 12:20 AM
# @Author  : huxiaoman
# @File    : 339_NestedListWeightSum.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        return self.dfs(nestedList, 1)

    def dfs(self, nestedList, depth):
        total = 0
        for item in nestedList:
            if item.isInteger():
                total += item.getInteger() * depth
            else:
                total += self.dfs(item.getList(), depth + 1)
        return total
