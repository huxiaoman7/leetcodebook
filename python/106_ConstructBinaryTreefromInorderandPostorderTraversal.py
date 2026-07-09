#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/6 10:50 AM
# @Author  : huxiaoman
# @File    : 106_ConstructBinaryTreefromInorderandPostorderTraversal.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        index = {value: i for i, value in enumerate(inorder)}
        self.post_index = len(postorder) - 1

        def build(left, right):
            if left > right:
                return None
            root_val = postorder[self.post_index]
            self.post_index -= 1
            root = TreeNode(root_val)
            mid = index[root_val]
            root.right = build(mid + 1, right)
            root.left = build(left, mid - 1)
            return root

        return build(0, len(inorder) - 1)
