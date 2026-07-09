#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 2:30 AM
# @Author  : huxiaoman
# @File    : 367_ValidPerfectSquare.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):

    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        left, right = 1, num
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            if square == num:
                return True
            if square < num:
                left = mid + 1
            else:
                right = mid - 1
        return False
