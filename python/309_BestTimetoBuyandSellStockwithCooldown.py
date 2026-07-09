#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 9:50 PM
# @Author  : huxiaoman
# @File    : 309_BestTimetoBuyandSellStockwithCooldown.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        hold = float('-inf')
        sold = 0
        rest = 0
        for price in prices:
            prev_sold = sold
            sold = hold + price
            hold = max(hold, rest - price)
            rest = max(rest, prev_sold)
        return max(sold, rest)
