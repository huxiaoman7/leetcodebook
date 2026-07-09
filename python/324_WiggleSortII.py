#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 11:05 PM
# @Author  : huxiaoman
# @File    : 324_WiggleSortII.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        sorted_nums = sorted(nums)
        half = (len(nums) + 1) // 2
        nums[::2] = sorted_nums[:half][::-1]
        nums[1::2] = sorted_nums[half:][::-1]
