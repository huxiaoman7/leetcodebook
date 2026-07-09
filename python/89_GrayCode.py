#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/5 11:10 AM
# @Author  : huxiaoman
# @File    : 89_GrayCode.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = [0]
        for i in range(n):
            add = 1 << i
            result += [add + num for num in reversed(result)]
        return result
