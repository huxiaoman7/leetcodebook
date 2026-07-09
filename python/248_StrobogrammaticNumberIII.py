#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 4:50 PM
# @Author  : huxiaoman
# @File    : 248_StrobogrammaticNumberIII.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        count = 0
        for length in range(len(low), len(high) + 1):
            for num in self.build(length, length):
                if (length == len(low) and num < low) or (length == len(high) and num > high):
                    continue
                count += 1
        return count

    def build(self, n, total):
        if n == 0:
            return ['']
        if n == 1:
            return ['0', '1', '8']
        result = []
        for middle in self.build(n - 2, total):
            for left, right in [('0', '0'), ('1', '1'), ('6', '9'), ('8', '8'), ('9', '6')]:
                if n == total and left == '0':
                    continue
                result.append(left + middle + right)
        return result
