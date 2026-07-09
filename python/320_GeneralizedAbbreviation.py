#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 10:45 PM
# @Author  : huxiaoman
# @File    : 320_GeneralizedAbbreviation.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        result = []
        self.backtrack(word, 0, '', 0, result)
        return result

    def backtrack(self, word, index, path, count, result):
        if index == len(word):
            if count:
                path += str(count)
            result.append(path)
            return

        self.backtrack(word, index + 1, path, count + 1, result)
        self.backtrack(word, index + 1, path + (str(count) if count else '') + word[index], 0, result)
