#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/6 10:40 AM
# @Author  : huxiaoman
# @File    : 105_ConstructBinaryTreefromPreorderandInorderTraversal.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        index = {value: i for i, value in enumerate(inorder)}
        self.pre_index = 0

        def build(left, right):
            if left > right:
                return None
            root_val = preorder[self.pre_index]
            self.pre_index += 1
            root = TreeNode(root_val)
            mid = index[root_val]
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)
            return root

        return build(0, len(inorder) - 1)
