#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 8:50 PM
# @Author  : huxiaoman
# @File    : 297_SerializeandDeserializeBinaryTree.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec(object):

    def serialize(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        values = []
        self.preorder(root, values)
        return ','.join(values)

    def preorder(self, node, values):
        if not node:
            values.append('#')
            return
        values.append(str(node.val))
        self.preorder(node.left, values)
        self.preorder(node.right, values)

    def deserialize(self, data):
        """
        :type data: str
        :rtype: TreeNode
        """
        values = iter(data.split(','))
        return self.build(values)

    def build(self, values):
        value = next(values)
        if value == '#':
            return None
        node = TreeNode(int(value))
        node.left = self.build(values)
        node.right = self.build(values)
        return node
