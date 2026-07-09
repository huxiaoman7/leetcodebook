#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/6 11:50 AM
# @Author  : huxiaoman
# @File    : 112_PathSum.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == sum
        return (self.hasPathSum(root.left, sum - root.val) or
                self.hasPathSum(root.right, sum - root.val))
