#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 12:05 AM
# @Author  : huxiaoman
# @File    : 336_PalindromePairs.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        lookup = {word: i for i, word in enumerate(words)}
        result = []
        for i, word in enumerate(words):
            for cut in range(len(word) + 1):
                prefix = word[:cut]
                suffix = word[cut:]
                if self.is_palindrome(prefix):
                    target = suffix[::-1]
                    if target in lookup and lookup[target] != i:
                        result.append([lookup[target], i])
                if cut != len(word) and self.is_palindrome(suffix):
                    target = prefix[::-1]
                    if target in lookup and lookup[target] != i:
                        result.append([i, lookup[target]])
        return result

    def is_palindrome(self, word):
        return word == word[::-1]
