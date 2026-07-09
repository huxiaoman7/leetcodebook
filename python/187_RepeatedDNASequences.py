#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 12:35 PM
# @Author  : huxiaoman
# @File    : 187_RepeatedDNASequences.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        seen = set()
        repeated = set()
        for i in range(len(s) - 9):
            sequence = s[i:i + 10]
            if sequence in seen:
                repeated.add(sequence)
            else:
                seen.add(sequence)
        return list(repeated)
