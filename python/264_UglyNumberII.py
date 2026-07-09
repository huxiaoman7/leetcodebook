#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 6:05 PM
# @Author  : huxiaoman
# @File    : 264_UglyNumberII.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ugly = [1]
        i2 = i3 = i5 = 0
        while len(ugly) < n:
            next_num = min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5)
            ugly.append(next_num)
            if next_num == ugly[i2] * 2:
                i2 += 1
            if next_num == ugly[i3] * 3:
                i3 += 1
            if next_num == ugly[i5] * 5:
                i5 += 1
        return ugly[-1]
