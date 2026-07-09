#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/6 10:10 AM
# @Author  : huxiaoman
# @File    : 102_BinaryTreeLevelOrderTraversal.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        result = []
        queue = [root]
        while queue:
            level = []
            next_queue = []
            for node in queue:
                level.append(node.val)
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            result.append(level)
            queue = next_queue
        return result
