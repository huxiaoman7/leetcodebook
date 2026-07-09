#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/8 12:10 PM
# @Author  : huxiaoman
# @File    : 156_BinaryTreeUpsideDown.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        parent = None
        parent_right = None
        cur = root
        while cur:
            next_left = cur.left
            cur.left = parent_right
            parent_right = cur.right
            cur.right = parent
            parent = cur
            cur = next_left
        return parent
