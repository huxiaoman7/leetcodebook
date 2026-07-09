#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/8 10:30 AM
# @Author  : huxiaoman
# @File    : 144_BinaryTreePreorderTraversal.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        result = []
        stack = [root]
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result
