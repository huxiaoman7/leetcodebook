#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 4:00 AM
# @Author  : huxiaoman
# @File    : 385_MiniParser.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class NestedInteger(object):

    def __init__(self, value=None):
        self.value = value
        self.items = [] if value is None else None

    def isInteger(self):
        return self.items is None

    def add(self, elem):
        if self.items is None:
            self.items = []
            self.value = None
        self.items.append(elem)

    def setInteger(self, value):
        self.value = value
        self.items = None

    def getInteger(self):
        return self.value if self.isInteger() else None

    def getList(self):
        return self.items if not self.isInteger() else None


class Solution(object):

    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        if not s:
            return NestedInteger()
        if s[0] != '[':
            return NestedInteger(int(s))
        stack = []
        number_start = None
        for i, ch in enumerate(s):
            if ch == '[':
                stack.append(NestedInteger())
            elif ch in '-0123456789':
                if number_start is None:
                    number_start = i
            elif ch in ',]':
                if number_start is not None:
                    stack[-1].add(NestedInteger(int(s[number_start:i])))
                    number_start = None
                if ch == ']' and len(stack) > 1:
                    item = stack.pop()
                    stack[-1].add(item)
        return stack[0]
