#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/8 12:20 PM
# @Author  : huxiaoman
# @File    : 157_ReadNCharactersGivenRead4.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


def read4(buf):
    return 0


class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        total = 0
        tmp = [''] * 4
        while total < n:
            count = read4(tmp)
            if count == 0:
                break
            for i in range(min(count, n - total)):
                buf[total] = tmp[i]
                total += 1
        return total
