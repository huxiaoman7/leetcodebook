#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/5 12:10 PM
# @Author  : huxiaoman
# @File    : 95_UniqueBinarySearchTreesII.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []

        def build(left, right):
            if left > right:
                return [None]
            result = []
            for root_val in range(left, right + 1):
                for left_node in build(left, root_val - 1):
                    for right_node in build(root_val + 1, right):
                        root = TreeNode(root_val)
                        root.left = left_node
                        root.right = right_node
                        result.append(root)
            return result

        return build(1, n)
