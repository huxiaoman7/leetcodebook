#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/8 12:30 PM
# @Author  : huxiaoman
# @File    : 158_ReadNCharactersGivenRead4II.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


def read4(buf):
    return 0


class Solution(object):
    def __init__(self):
        self.cache = []

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        total = 0
        while total < n:
            if self.cache:
                buf[total] = self.cache.pop(0)
                total += 1
                continue
            tmp = [''] * 4
            count = read4(tmp)
            if count == 0:
                break
            self.cache.extend(tmp[:count])
        return total
