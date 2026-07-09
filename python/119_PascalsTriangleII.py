#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/6 1:00 PM
# @Author  : huxiaoman
# @File    : 119_PascalsTriangleII.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        for _ in range(rowIndex):
            row = [1] + [row[i] + row[i + 1] for i in range(len(row) - 1)] + [1]
        return row
