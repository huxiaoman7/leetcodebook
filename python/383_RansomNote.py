#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 3:50 AM
# @Author  : huxiaoman
# @File    : 383_RansomNote.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


from collections import Counter


class Solution(object):

    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        need = Counter(ransomNote)
        have = Counter(magazine)
        for ch, count in need.items():
            if have[ch] < count:
                return False
        return True
