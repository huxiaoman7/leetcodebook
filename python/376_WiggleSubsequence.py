#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 3:15 AM
# @Author  : huxiaoman
# @File    : 376_WiggleSubsequence.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):

    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        up = down = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                up = down + 1
            elif nums[i] < nums[i - 1]:
                down = up + 1
        return max(up, down)
