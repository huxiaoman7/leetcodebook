#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/7 10:50 AM
# @Author  : huxiaoman
# @File    : 126_WordLadderII.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        word_set = set(wordList)
        if endWord not in word_set:
            return []
        parents = {}
        level = set([beginWord])
        found = False
        while level and not found:
            word_set -= level
            next_level = set()
            for word in level:
                for i in range(len(word)):
                    for ch in 'abcdefghijklmnopqrstuvwxyz':
                        nxt = word[:i] + ch + word[i + 1:]
                        if nxt not in word_set:
                            continue
                        if nxt == endWord:
                            found = True
                        next_level.add(nxt)
                        parents.setdefault(nxt, []).append(word)
            level = next_level

        result = []

        def build(word, path):
            if word == beginWord:
                result.append(path[::-1])
                return
            for parent in parents.get(word, []):
                build(parent, path + [parent])

        if found:
            build(endWord, [endWord])
        return result
