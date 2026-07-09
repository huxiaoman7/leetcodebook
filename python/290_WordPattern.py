#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 8:15 PM
# @Author  : huxiaoman
# @File    : 290_WordPattern.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split()
        if len(pattern) != len(words):
            return False
        p_to_w = {}
        w_to_p = {}
        for p, word in zip(pattern, words):
            if p_to_w.get(p, word) != word or w_to_p.get(word, p) != p:
                return False
            p_to_w[p] = word
            w_to_p[word] = p
        return True
