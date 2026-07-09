#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 12:30 AM
# @Author  : huxiaoman
# @File    : 341_FlattenNestedListIterator.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class NestedIterator(object):

    def __init__(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        """
        self.stack = nestedList[::-1]

    def next(self):
        """
        :rtype: int
        """
        return self.stack.pop().getInteger()

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.stack:
            top = self.stack[-1]
            if top.isInteger():
                return True
            self.stack.pop()
            self.stack.extend(top.getList()[::-1])
        return False
