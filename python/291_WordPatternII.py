#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 8:20 PM
# @Author  : huxiaoman
# @File    : 291_WordPatternII.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def wordPatternMatch(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        return self.backtrack(pattern, 0, s, 0, {}, set())

    def backtrack(self, pattern, p_index, s, s_index, mapping, used):
        if p_index == len(pattern) and s_index == len(s):
            return True
        if p_index == len(pattern) or s_index == len(s):
            return False

        ch = pattern[p_index]
        if ch in mapping:
            word = mapping[ch]
            if not s.startswith(word, s_index):
                return False
            return self.backtrack(pattern, p_index + 1, s, s_index + len(word), mapping, used)

        for end in range(s_index + 1, len(s) + 1):
            word = s[s_index:end]
            if word in used:
                continue
            mapping[ch] = word
            used.add(word)
            if self.backtrack(pattern, p_index + 1, s, end, mapping, used):
                return True
            used.remove(word)
            del mapping[ch]
        return False
