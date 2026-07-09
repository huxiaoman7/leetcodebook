#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/5 12:00 PM
# @Author  : huxiaoman
# @File    : 94_BinaryTreeInorderTraversal.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            result.append(cur.val)
            cur = cur.right
        return result
