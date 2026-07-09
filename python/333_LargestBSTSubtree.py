#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 11:50 PM
# @Author  : huxiaoman
# @File    : 333_LargestBSTSubtree.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.best = 0
        self.helper(root)
        return self.best

    def helper(self, node):
        if not node:
            return True, 0, float('inf'), float('-inf')
        left_bst, left_size, left_min, left_max = self.helper(node.left)
        right_bst, right_size, right_min, right_max = self.helper(node.right)
        if left_bst and right_bst and left_max < node.val < right_min:
            size = left_size + right_size + 1
            self.best = max(self.best, size)
            return True, size, min(left_min, node.val), max(right_max, node.val)
        return False, 0, 0, 0
