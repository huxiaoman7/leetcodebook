#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 7:10 PM
# @Author  : huxiaoman
# @File    : 277_FindtheCelebrity.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


def knows(a, b):
    return False


class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        candidate = 0
        for i in range(1, n):
            if knows(candidate, i):
                candidate = i
        for i in range(n):
            if i != candidate and (knows(candidate, i) or not knows(i, candidate)):
                return -1
        return candidate
