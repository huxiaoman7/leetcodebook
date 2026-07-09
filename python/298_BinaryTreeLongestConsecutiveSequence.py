#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 8:55 PM
# @Author  : huxiaoman
# @File    : 298_BinaryTreeLongestConsecutiveSequence.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.longest = 0
        self.dfs(root, None, 0)
        return self.longest

    def dfs(self, node, parent, length):
        if not node:
            return
        if parent and node.val == parent.val + 1:
            length += 1
        else:
            length = 1
        self.longest = max(self.longest, length)
        self.dfs(node.left, node, length)
        self.dfs(node.right, node, length)
