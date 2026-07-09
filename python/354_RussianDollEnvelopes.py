#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 1:35 AM
# @Author  : huxiaoman
# @File    : 354_RussianDollEnvelopes.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


import bisect


class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        envelopes.sort(key=lambda item: (item[0], -item[1]))
        tails = []
        for _, height in envelopes:
            index = bisect.bisect_left(tails, height)
            if index == len(tails):
                tails.append(height)
            else:
                tails[index] = height
        return len(tails)
