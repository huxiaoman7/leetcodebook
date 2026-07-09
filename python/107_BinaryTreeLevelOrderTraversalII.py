#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/6 11:00 AM
# @Author  : huxiaoman
# @File    : 107_BinaryTreeLevelOrderTraversalII.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        result = []
        queue = [root]
        while queue:
            result.append([node.val for node in queue])
            next_queue = []
            for node in queue:
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            queue = next_queue
        return result[::-1]
