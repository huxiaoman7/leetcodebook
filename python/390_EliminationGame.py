#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 4:25 AM
# @Author  : huxiaoman
# @File    : 390_EliminationGame.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):

    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        head = 1
        step = 1
        left = True
        remaining = n
        while remaining > 1:
            if left or remaining % 2 == 1:
                head += step
            step *= 2
            remaining //= 2
            left = not left
        return head
