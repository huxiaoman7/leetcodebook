#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 2:55 AM
# @Author  : huxiaoman
# @File    : 372_SuperPow.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):

    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        mod = 1337
        result = 1
        a %= mod
        for digit in b:
            result = pow(result, 10, mod) * pow(a, digit, mod) % mod
        return result
