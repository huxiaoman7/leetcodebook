#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 2:05 PM
# @Author  : huxiaoman
# @File    : 213_HouseRobberII.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return nums[0] if nums else 0
        return max(self.rob_line(nums[:-1]), self.rob_line(nums[1:]))

    def rob_line(self, nums):
        prev, curr = 0, 0
        for num in nums:
            prev, curr = curr, max(curr, prev + num)
        return curr
