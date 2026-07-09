#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/8 12:00 PM
# @Author  : huxiaoman
# @File    : 154_FindMinimuminRotatedSortedArrayII.py
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
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right -= 1
        return nums[left]
