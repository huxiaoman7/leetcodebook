#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 2:35 PM
# @Author  : huxiaoman
# @File    : 219_ContainsDuplicateII.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        indexes = {}
        for i, num in enumerate(nums):
            if num in indexes and i - indexes[num] <= k:
                return True
            indexes[num] = i
        return False
