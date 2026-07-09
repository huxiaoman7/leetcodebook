#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 9:05 PM
# @Author  : huxiaoman
# @File    : 300_LongestIncreasingSubsequence.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


import bisect


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tails = []
        for num in nums:
            index = bisect.bisect_left(tails, num)
            if index == len(tails):
                tails.append(num)
            else:
                tails[index] = num
        return len(tails)
