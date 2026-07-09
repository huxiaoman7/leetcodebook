#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 4:25 PM
# @Author  : huxiaoman
# @File    : 243_ShortestWordDistance.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        index1 = index2 = -1
        result = len(words)
        for i, word in enumerate(words):
            if word == word1:
                index1 = i
            if word == word2:
                index2 = i
            if index1 != -1 and index2 != -1:
                result = min(result, abs(index1 - index2))
        return result
