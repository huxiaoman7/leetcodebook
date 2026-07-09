#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 7:15 PM
# @Author  : huxiaoman
# @File    : 278_FirstBadVersion.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


def isBadVersion(version):
    return False


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left
