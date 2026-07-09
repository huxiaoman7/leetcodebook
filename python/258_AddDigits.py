#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 5:40 PM
# @Author  : huxiaoman
# @File    : 258_AddDigits.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        return 0 if num == 0 else 1 + (num - 1) % 9
