#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 7:40 PM
# @Author  : huxiaoman
# @File    : 283_MoveZeroes.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        insert = 0
        for num in nums:
            if num != 0:
                nums[insert] = num
                insert += 1
        for i in range(insert, len(nums)):
            nums[i] = 0
