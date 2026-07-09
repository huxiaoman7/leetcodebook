#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 3:30 PM
# @Author  : huxiaoman
# @File    : 230_KthSmallestElementinaBST.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right
        return None
