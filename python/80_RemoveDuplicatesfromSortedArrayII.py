#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/4 1:10 PM
# @Author  : huxiaoman
# @File    : 80_RemoveDuplicatesfromSortedArrayII.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)
        index = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[index - 2]:
                nums[index] = nums[i]
                index += 1
        return index
