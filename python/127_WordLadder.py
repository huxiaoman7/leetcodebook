#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/7 11:00 AM
# @Author  : huxiaoman
# @File    : 127_WordLadder.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
        queue = [(beginWord, 1)]
        visited = set([beginWord])
        for word, depth in queue:
            if word == endWord:
                return depth
            for i in range(len(word)):
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    nxt = word[:i] + ch + word[i + 1:]
                    if nxt in word_set and nxt not in visited:
                        visited.add(nxt)
                        queue.append((nxt, depth + 1))
        return 0
