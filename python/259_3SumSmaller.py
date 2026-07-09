#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 5:45 PM
# @Author  : huxiaoman
# @File    : 259_3SumSmaller.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        result = 0
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] < target:
                    result += right - left
                    left += 1
                else:
                    right -= 1
        return result
