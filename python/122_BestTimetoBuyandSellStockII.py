#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/7 10:10 AM
# @Author  : huxiaoman
# @File    : 122_BestTimetoBuyandSellStockII.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        result = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                result += prices[i] - prices[i - 1]
        return result
