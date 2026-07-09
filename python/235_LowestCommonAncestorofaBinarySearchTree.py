#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 3:50 PM
# @Author  : huxiaoman
# @File    : 235_LowestCommonAncestorofaBinarySearchTree.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root
        return None
