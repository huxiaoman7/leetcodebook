#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/4 10:50 AM
# @Author  : huxiaoman
# @File    : 66_PlusOne.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            total = digits[i] + carry
            digits[i] = total % 10
            carry = total // 10
            if carry == 0:
                return digits
        return [1] + digits
