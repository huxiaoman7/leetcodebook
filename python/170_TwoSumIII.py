#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 11:30 AM
# @Author  : huxiaoman
# @File    : 170_TwoSumIII.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class TwoSum(object):

    def __init__(self):
        self.count = {}

    def add(self, number):
        """
        :type number: int
        :rtype: void
        """
        self.count[number] = self.count.get(number, 0) + 1

    def find(self, value):
        """
        :type value: int
        :rtype: bool
        """
        for num in self.count:
            other = value - num
            if other != num and other in self.count:
                return True
            if other == num and self.count[num] > 1:
                return True
        return False
