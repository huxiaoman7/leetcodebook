#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/28 3:33 PM
# @Author  : huxiaoman
# @File    : 6_ZigZagConversion.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        L = [''] * numRows
        index, step = 0, 1

        for x in s:
            L[index] += x
            if index == 0:
                step = 1
            elif index == numRows -1:
                step = -1
            index += step

        return ''.join(L)

if __name__ == '__main__':
    s = Solution()
    print s.convert("PAYPALISHIRING",3)
