#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 4:15 AM
# @Author  : huxiaoman
# @File    : 388_LongestAbsoluteFilePath.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):

    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        result = 0
        lengths = {0: 0}
        for item in input.split('\n'):
            name = item.lstrip('\t')
            depth = len(item) - len(name)
            lengths[depth + 1] = lengths[depth] + len(name) + 1
            if '.' in name:
                result = max(result, lengths[depth + 1] - 1)
        return result
