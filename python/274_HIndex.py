#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 6:55 PM
# @Author  : huxiaoman
# @File    : 274_HIndex.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse=True)
        h = 0
        for i, citation in enumerate(citations, 1):
            if citation >= i:
                h = i
            else:
                break
        return h
