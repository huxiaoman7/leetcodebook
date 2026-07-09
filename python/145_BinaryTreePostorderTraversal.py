#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/8 10:40 AM
# @Author  : huxiaoman
# @File    : 145_BinaryTreePostorderTraversal.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def postorderTraversal(self, root):
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
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return result[::-1]
