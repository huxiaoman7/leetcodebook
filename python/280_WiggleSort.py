#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 7:25 PM
# @Author  : huxiaoman
# @File    : 280_WiggleSort.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 1):
            if (i % 2 == 0 and nums[i] > nums[i + 1]) or (i % 2 == 1 and nums[i] < nums[i + 1]):
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
