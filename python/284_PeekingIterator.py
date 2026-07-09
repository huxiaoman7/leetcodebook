#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 7:45 PM
# @Author  : huxiaoman
# @File    : 284_PeekingIterator.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class PeekingIterator(object):
    def __init__(self, iterator):
        """
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.cache = None
        self.has_cache = False

    def peek(self):
        """
        :rtype: int
        """
        if not self.has_cache:
            self.cache = self.iterator.next()
            self.has_cache = True
        return self.cache

    def next(self):
        """
        :rtype: int
        """
        if self.has_cache:
            self.has_cache = False
            return self.cache
        return self.iterator.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.has_cache or self.iterator.hasNext()
