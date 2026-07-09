#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/5 12:40 PM
# @Author  : huxiaoman
# @File    : 98_ValidateBinarySearchTree.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack = []
        cur = root
        prev = None
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if prev is not None and cur.val <= prev:
                return False
            prev = cur.val
            cur = cur.right
        return True
