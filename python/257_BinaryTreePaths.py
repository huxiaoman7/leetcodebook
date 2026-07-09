#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 5:35 PM
# @Author  : huxiaoman
# @File    : 257_BinaryTreePaths.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        result = []
        self.dfs(root, str(root.val), result)
        return result

    def dfs(self, node, path, result):
        if not node.left and not node.right:
            result.append(path)
            return
        if node.left:
            self.dfs(node.left, path + '->' + str(node.left.val), result)
        if node.right:
            self.dfs(node.right, path + '->' + str(node.right.val), result)
