#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 10:05 PM
# @Author  : huxiaoman
# @File    : 312_BurstBalloons.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + [num for num in nums if num > 0] + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for length in range(2, n):
            for left in range(n - length):
                right = left + length
                for i in range(left + 1, right):
                    dp[left][right] = max(dp[left][right], nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right])
        return dp[0][n - 1]
