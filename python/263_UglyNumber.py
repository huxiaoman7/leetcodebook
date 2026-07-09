#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 6:00 PM
# @Author  : huxiaoman
# @File    : 263_UglyNumber.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        for factor in [2, 3, 5]:
            while num % factor == 0:
                num //= factor
        return num == 1
