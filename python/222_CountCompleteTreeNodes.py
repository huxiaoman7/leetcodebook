#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 2:50 PM
# @Author  : huxiaoman
# @File    : 222_CountCompleteTreeNodes.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        if left_height == right_height:
            return (1 << left_height) + self.countNodes(root.right)
        return (1 << right_height) + self.countNodes(root.left)

    def height(self, node):
        height = 0
        while node:
            height += 1
            node = node.left
        return height
