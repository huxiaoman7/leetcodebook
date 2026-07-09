#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/3 12:30 PM
# @Author  : huxiaoman
# @File    : 60_PermutationSequence.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = [str(i) for i in range(1, n + 1)]
        factorial = [1] * (n + 1)
        for i in range(1, n + 1):
            factorial[i] = factorial[i - 1] * i

        k -= 1
        result = []
        for i in range(n, 0, -1):
            index = k // factorial[i - 1]
            k %= factorial[i - 1]
            result.append(nums.pop(index))
        return ''.join(result)
