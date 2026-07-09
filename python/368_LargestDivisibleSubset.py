#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 2:35 AM
# @Author  : huxiaoman
# @File    : 368_LargestDivisibleSubset.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):

    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        nums.sort()
        n = len(nums)
        dp = [1] * n
        parent = [-1] * n
        best = 0
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    parent[i] = j
            if dp[i] > dp[best]:
                best = i
        result = []
        while best != -1:
            result.append(nums[best])
            best = parent[best]
        return result[::-1]
