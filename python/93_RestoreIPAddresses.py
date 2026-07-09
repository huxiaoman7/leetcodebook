#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/5 11:50 AM
# @Author  : huxiaoman
# @File    : 93_RestoreIPAddresses.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []

        def valid(part):
            return part == '0' or (part[0] != '0' and int(part) <= 255)

        def dfs(index, path):
            if len(path) == 4:
                if index == len(s):
                    result.append('.'.join(path))
                return
            remain = len(s) - index
            if remain < 4 - len(path) or remain > 3 * (4 - len(path)):
                return
            for length in range(1, 4):
                part = s[index:index + length]
                if len(part) == length and valid(part):
                    dfs(index + length, path + [part])

        dfs(0, [])
        return result
