#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 4:55 PM
# @Author  : huxiaoman
# @File    : 249_GroupShiftedStrings.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


from collections import defaultdict


class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        groups = defaultdict(list)
        for string in strings:
            key = tuple((ord(ch) - ord(string[0])) % 26 for ch in string)
            groups[key].append(string)
        return list(groups.values())
