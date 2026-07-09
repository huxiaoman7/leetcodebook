#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 2:40 PM
# @Author  : huxiaoman
# @File    : 220_ContainsDuplicateIII.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k <= 0 or t < 0:
            return False

        width = t + 1
        buckets = {}
        for i, num in enumerate(nums):
            bucket = num // width
            if bucket in buckets:
                return True
            if bucket - 1 in buckets and abs(num - buckets[bucket - 1]) <= t:
                return True
            if bucket + 1 in buckets and abs(num - buckets[bucket + 1]) <= t:
                return True

            buckets[bucket] = num
            if i >= k:
                old_bucket = nums[i - k] // width
                del buckets[old_bucket]
        return False
