#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 9:35 PM
# @Author  : huxiaoman
# @File    : 306_AdditiveNumber.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        for i in range(1, n):
            for j in range(i + 1, n):
                first = num[:i]
                second = num[i:j]
                if (len(first) > 1 and first[0] == '0') or (len(second) > 1 and second[0] == '0'):
                    continue
                if self.valid(int(first), int(second), num[j:]):
                    return True
        return False

    def valid(self, first, second, rest):
        while rest:
            total = first + second
            total_string = str(total)
            if not rest.startswith(total_string):
                return False
            rest = rest[len(total_string):]
            first, second = second, total
        return True
