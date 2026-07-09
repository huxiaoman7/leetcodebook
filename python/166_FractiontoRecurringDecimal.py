#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 10:50 AM
# @Author  : huxiaoman
# @File    : 166_FractiontoRecurringDecimal.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0:
            return '0'
        result = []
        if (numerator < 0) ^ (denominator < 0):
            result.append('-')
        numerator, denominator = abs(numerator), abs(denominator)
        result.append(str(numerator // denominator))
        remainder = numerator % denominator
        if remainder == 0:
            return ''.join(result)
        result.append('.')
        seen = {}
        while remainder:
            if remainder in seen:
                result.insert(seen[remainder], '(')
                result.append(')')
                break
            seen[remainder] = len(result)
            remainder *= 10
            result.append(str(remainder // denominator))
            remainder %= denominator
        return ''.join(result)
