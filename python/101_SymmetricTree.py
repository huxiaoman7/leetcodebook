#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/6 10:00 AM
# @Author  : huxiaoman
# @File    : 101_SymmetricTree.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return (left.val == right.val and
                    helper(left.left, right.right) and
                    helper(left.right, right.left))

        return True if not root else helper(root.left, root.right)
