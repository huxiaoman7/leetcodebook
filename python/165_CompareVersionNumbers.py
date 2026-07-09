#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 10:40 AM
# @Author  : huxiaoman
# @File    : 165_CompareVersionNumbers.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        nums1 = version1.split('.')
        nums2 = version2.split('.')
        size = max(len(nums1), len(nums2))
        for i in range(size):
            a = int(nums1[i]) if i < len(nums1) else 0
            b = int(nums2[i]) if i < len(nums2) else 0
            if a < b:
                return -1
            if a > b:
                return 1
        return 0
