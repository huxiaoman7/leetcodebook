#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/6 11:40 AM
# @Author  : huxiaoman
# @File    : 111_MinimumDepthofBinaryTree.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left:
            return self.minDepth(root.right) + 1
        if not root.right:
            return self.minDepth(root.left) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
