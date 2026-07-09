#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 4:45 PM
# @Author  : huxiaoman
# @File    : 247_StrobogrammaticNumberII.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return self.build(n, n)

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
