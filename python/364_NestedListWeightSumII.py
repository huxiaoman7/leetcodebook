#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 2:15 AM
# @Author  : huxiaoman
# @File    : 364_NestedListWeightSumII.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):

    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        unweighted = 0
        weighted = 0
        level = nestedList
        while level:
            next_level = []
            for item in level:
                if item.isInteger():
                    unweighted += item.getInteger()
                else:
                    next_level.extend(item.getList())
            weighted += unweighted
            level = next_level
        return weighted
