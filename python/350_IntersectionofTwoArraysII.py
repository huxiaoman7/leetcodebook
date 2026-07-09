#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 1:15 AM
# @Author  : huxiaoman
# @File    : 350_IntersectionofTwoArraysII.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


from collections import Counter


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        counter = Counter(nums1) & Counter(nums2)
        result = []
        for num, count in counter.items():
            result.extend([num] * count)
        return result
