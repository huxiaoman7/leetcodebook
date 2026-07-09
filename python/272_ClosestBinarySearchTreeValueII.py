#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 6:45 PM
# @Author  : huxiaoman
# @File    : 272_ClosestBinarySearchTreeValueII.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        values = []
        self.inorder(root, values)
        values.sort(key=lambda value: abs(value - target))
        return values[:k]

    def inorder(self, node, values):
        if not node:
            return
        self.inorder(node.left, values)
        values.append(node.val)
        self.inorder(node.right, values)
