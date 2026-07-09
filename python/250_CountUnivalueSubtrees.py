#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 5:00 PM
# @Author  : huxiaoman
# @File    : 250_CountUnivalueSubtrees.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.count = 0
        self.is_unival(root)
        return self.count

    def is_unival(self, node):
        if not node:
            return True
        left = self.is_unival(node.left)
        right = self.is_unival(node.right)
        if left and right:
            if node.left and node.left.val != node.val:
                return False
            if node.right and node.right.val != node.val:
                return False
            self.count += 1
            return True
        return False
