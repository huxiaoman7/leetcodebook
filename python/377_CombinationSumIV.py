#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 3:20 AM
# @Author  : huxiaoman
# @File    : 377_CombinationSumIV.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):

    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [0] * (target + 1)
        dp[0] = 1
        for total in range(1, target + 1):
            for num in nums:
                if total >= num:
                    dp[total] += dp[total - num]
        return dp[target]
