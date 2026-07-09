#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 1:15 PM
# @Author  : huxiaoman
# @File    : 202_HappyNumber.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = sum(int(ch) ** 2 for ch in str(n))
        return n == 1
