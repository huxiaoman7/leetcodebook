#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 4:40 AM
# @Author  : huxiaoman
# @File    : 393_UTF8Validation.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):

    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        remaining = 0
        for num in data:
            num &= 255
            if remaining:
                if num >> 6 != 0b10:
                    return False
                remaining -= 1
            else:
                if num >> 7 == 0:
                    remaining = 0
                elif num >> 5 == 0b110:
                    remaining = 1
                elif num >> 4 == 0b1110:
                    remaining = 2
                elif num >> 3 == 0b11110:
                    remaining = 3
                else:
                    return False
        return remaining == 0
