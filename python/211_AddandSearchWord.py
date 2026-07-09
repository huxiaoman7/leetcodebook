#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 1:55 PM
# @Author  : huxiaoman
# @File    : 211_AddandSearchWord.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class WordDictionary(object):

    def __init__(self):
        self.root = {}

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.root
        for ch in word:
            node = node.setdefault(ch, {})
        node['#'] = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return self.dfs(word, 0, self.root)

    def dfs(self, word, index, node):
        if index == len(word):
            return '#' in node
        ch = word[index]
        if ch == '.':
            return any(self.dfs(word, index + 1, child) for key, child in node.items() if key != '#')
        return ch in node and self.dfs(word, index + 1, node[ch])
