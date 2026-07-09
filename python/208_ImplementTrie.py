#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 1:40 PM
# @Author  : huxiaoman
# @File    : 208_ImplementTrie.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Trie(object):

    def __init__(self):
        self.root = {}

    def insert(self, word):
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
        node = self.find(word)
        return node is not None and '#' in node

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        return self.find(prefix) is not None

    def find(self, word):
        node = self.root
        for ch in word:
            if ch not in node:
                return None
            node = node[ch]
        return node
