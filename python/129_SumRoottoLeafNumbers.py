#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/7 11:20 AM
# @Author  : huxiaoman
# @File    : 129_SumRoottoLeafNumbers.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, total):
            if not node:
                return 0
            total = total * 10 + node.val
            if not node.left and not node.right:
                return total
            return dfs(node.left, total) + dfs(node.right, total)

        return dfs(root, 0)
