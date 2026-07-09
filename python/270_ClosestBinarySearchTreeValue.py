#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 6:35 PM
# @Author  : huxiaoman
# @File    : 270_ClosestBinarySearchTreeValue.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        closest = root.val
        while root:
            if abs(root.val - target) < abs(closest - target):
                closest = root.val
            root = root.left if target < root.val else root.right
        return closest
