#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/7 10:30 AM
# @Author  : huxiaoman
# @File    : 124_BinaryTreeMaximumPathSum.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = float('-inf')

        def dfs(node):
            if not node:
                return 0
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            self.result = max(self.result, node.val + left + right)
            return node.val + max(left, right)

        dfs(root)
        return self.result
