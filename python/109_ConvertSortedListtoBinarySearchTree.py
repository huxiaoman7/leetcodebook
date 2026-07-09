#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/6 11:20 AM
# @Author  : huxiaoman
# @File    : 109_ConvertSortedListtoBinarySearchTree.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        def build(left, right):
            if left > right:
                return None
            mid = left + (right - left) // 2
            root = TreeNode(nums[mid])
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)
            return root

        return build(0, len(nums) - 1)
