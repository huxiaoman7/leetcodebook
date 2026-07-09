#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/7 10:00 AM
# @Author  : huxiaoman
# @File    : 121_BestTimetoBuyandSellStock.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = float('inf')
        result = 0
        for price in prices:
            min_price = min(min_price, price)
            result = max(result, price - min_price)
        return result
