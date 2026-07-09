#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 10:50 PM
# @Author  : huxiaoman
# @File    : 321_CreateMaximumNumber.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        result = []
        for i in range(max(0, k - len(nums2)), min(k, len(nums1)) + 1):
            result = max(result, self.merge(self.pick(nums1, i), self.pick(nums2, k - i)))
        return result

    def pick(self, nums, k):
        drop = len(nums) - k
        stack = []
        for num in nums:
            while drop and stack and stack[-1] < num:
                stack.pop()
                drop -= 1
            stack.append(num)
        return stack[:k]

    def merge(self, nums1, nums2):
        result = []
        while nums1 or nums2:
            if nums1 > nums2:
                result.append(nums1.pop(0))
            else:
                result.append(nums2.pop(0))
        return result
