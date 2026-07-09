#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 6:10 PM
# @Author  : huxiaoman
# @File    : 265_PaintHouseII.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:
            return 0
        prev_min = prev_second = 0
        prev_index = -1
        for row in costs:
            curr_min = curr_second = float('inf')
            curr_index = -1
            for i, cost in enumerate(row):
                total = cost + (prev_second if i == prev_index else prev_min)
                if total < curr_min:
                    curr_second = curr_min
                    curr_min = total
                    curr_index = i
                elif total < curr_second:
                    curr_second = total
            prev_min, prev_second, prev_index = curr_min, curr_second, curr_index
        return prev_min
