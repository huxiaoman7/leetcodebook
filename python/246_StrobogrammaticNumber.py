#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 4:40 PM
# @Author  : huxiaoman
# @File    : 246_StrobogrammaticNumber.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        pairs = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        left, right = 0, len(num) - 1
        while left <= right:
            if num[left] not in pairs or pairs[num[left]] != num[right]:
                return False
            left += 1
            right -= 1
        return True
