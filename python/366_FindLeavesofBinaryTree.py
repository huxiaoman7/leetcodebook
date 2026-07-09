#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 2:25 AM
# @Author  : huxiaoman
# @File    : 366_FindLeavesofBinaryTree.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):

    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []

        def height(node):
            if not node:
                return -1
            h = max(height(node.left), height(node.right)) + 1
            if h == len(result):
                result.append([])
            result[h].append(node.val)
            return h

        height(root)
        return result
