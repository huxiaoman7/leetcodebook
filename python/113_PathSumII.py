#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/6 12:00 PM
# @Author  : huxiaoman
# @File    : 113_PathSumII.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        result = []

        def dfs(node, target, path):
            if not node:
                return
            path.append(node.val)
            if not node.left and not node.right and node.val == target:
                result.append(path[:])
            dfs(node.left, target - node.val, path)
            dfs(node.right, target - node.val, path)
            path.pop()

        dfs(root, sum, [])
        return result
