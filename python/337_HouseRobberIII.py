#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 12:10 AM
# @Author  : huxiaoman
# @File    : 337_HouseRobberIII.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        rob, skip = self.dfs(root)
        return max(rob, skip)

    def dfs(self, node):
        if not node:
            return 0, 0
        left_rob, left_skip = self.dfs(node.left)
        right_rob, right_skip = self.dfs(node.right)
        rob = node.val + left_skip + right_skip
        skip = max(left_rob, left_skip) + max(right_rob, right_skip)
        return rob, skip
