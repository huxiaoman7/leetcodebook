#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/8 11:50 AM
# @Author  : huxiaoman
# @File    : 153_FindMinimuminRotatedSortedArray.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
