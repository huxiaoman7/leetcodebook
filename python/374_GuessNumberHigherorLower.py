#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 3:05 AM
# @Author  : huxiaoman
# @File    : 374_GuessNumberHigherorLower.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


def guess(num):
    return 0


class Solution(object):

    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            check = guess(mid)
            if check == 0:
                return mid
            if check < 0:
                right = mid - 1
            else:
                left = mid + 1
        return -1
