#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 4:35 PM
# @Author  : huxiaoman
# @File    : 245_ShortestWordDistanceIII.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        result = len(words)
        if word1 == word2:
            prev = -1
            for i, word in enumerate(words):
                if word == word1:
                    if prev != -1:
                        result = min(result, i - prev)
                    prev = i
            return result

        index1 = index2 = -1
        for i, word in enumerate(words):
            if word == word1:
                index1 = i
            elif word == word2:
                index2 = i
            if index1 != -1 and index2 != -1:
                result = min(result, abs(index1 - index2))
        return result
