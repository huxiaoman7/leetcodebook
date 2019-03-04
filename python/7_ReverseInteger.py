#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/28 3:34 PM
# @Author  : huxiaoman
# @File    : 7_ReverseInteger.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = 1 if x>=0 else -1
        new ,x = 0, abs(x)
        while x:
            new = 10 *new + x % 10
            x /= 10
        new = flag * new
        return new if new < 2147483648 and new >= -2147483648 else 0

if __name__ == '__main__':
    s = Solution()
    print s.reverse(3213424)
