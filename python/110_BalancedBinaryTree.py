#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/6 11:30 AM
# @Author  : huxiaoman
# @File    : 110_BalancedBinaryTree.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def depth(node):
            if not node:
                return 0
            left = depth(node.left)
            if left == -1:
                return -1
            right = depth(node.right)
            if right == -1 or abs(left - right) > 1:
                return -1
            return max(left, right) + 1

        return depth(root) != -1
