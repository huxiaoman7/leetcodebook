#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 4:30 PM
# @Author  : huxiaoman
# @File    : 244_ShortestWordDistanceII.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


from collections import defaultdict


class WordDistance(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.indexes = defaultdict(list)
        for i, word in enumerate(words):
            self.indexes[word].append(i)

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        indexes1 = self.indexes[word1]
        indexes2 = self.indexes[word2]
        i = j = 0
        result = float('inf')
        while i < len(indexes1) and j < len(indexes2):
            result = min(result, abs(indexes1[i] - indexes2[j]))
            if indexes1[i] < indexes2[j]:
                i += 1
            else:
                j += 1
        return result
