#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 8:00 PM
# @Author  : huxiaoman
# @File    : 287_FindtheDuplicateNumber.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        fast = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
