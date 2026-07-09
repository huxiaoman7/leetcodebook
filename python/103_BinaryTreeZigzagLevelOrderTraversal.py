#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/6 10:20 AM
# @Author  : huxiaoman
# @File    : 103_BinaryTreeZigzagLevelOrderTraversal.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        result = []
        queue = [root]
        left_to_right = True
        while queue:
            level = [node.val for node in queue]
            result.append(level if left_to_right else level[::-1])
            next_queue = []
            for node in queue:
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            queue = next_queue
            left_to_right = not left_to_right
        return result
