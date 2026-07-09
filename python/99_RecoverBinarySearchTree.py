#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/5 12:50 PM
# @Author  : huxiaoman
# @File    : 99_RecoverBinarySearchTree.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        stack = []
        cur = root
        prev = None
        first = None
        second = None
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if prev and prev.val > cur.val:
                if not first:
                    first = prev
                second = cur
            prev = cur
            cur = cur.right
        if first and second:
            first.val, second.val = second.val, first.val
