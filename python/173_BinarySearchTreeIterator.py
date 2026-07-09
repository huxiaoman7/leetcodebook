#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 12:00 PM
# @Author  : huxiaoman
# @File    : 173_BinarySearchTreeIterator.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.pushLeft(root)

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) > 0

    def next(self):
        """
        :rtype: int
        """
        node = self.stack.pop()
        self.pushLeft(node.right)
        return node.val

    def pushLeft(self, node):
        while node:
            self.stack.append(node)
            node = node.left
