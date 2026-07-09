#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 10:10 PM
# @Author  : huxiaoman
# @File    : 313_SuperUglyNumber.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        ugly = [1]
        indexes = [0] * len(primes)
        while len(ugly) < n:
            next_num = min(primes[i] * ugly[indexes[i]] for i in range(len(primes)))
            ugly.append(next_num)
            for i in range(len(primes)):
                if primes[i] * ugly[indexes[i]] == next_num:
                    indexes[i] += 1
        return ugly[-1]
