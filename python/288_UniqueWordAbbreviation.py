#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 8:05 PM
# @Author  : huxiaoman
# @File    : 288_UniqueWordAbbreviation.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class ValidWordAbbr(object):

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        self.abbr = {}
        for word in set(dictionary):
            key = self.get_abbr(word)
            if key in self.abbr and self.abbr[key] != word:
                self.abbr[key] = None
            else:
                self.abbr[key] = word

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        key = self.get_abbr(word)
        return key not in self.abbr or self.abbr[key] == word

    def get_abbr(self, word):
        if len(word) <= 2:
            return word
        return word[0] + str(len(word) - 2) + word[-1]
