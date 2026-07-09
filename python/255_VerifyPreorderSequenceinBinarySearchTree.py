#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 5:25 PM
# @Author  : huxiaoman
# @File    : 255_VerifyPreorderSequenceinBinarySearchTree.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        lower = float('-inf')
        stack = []
        for value in preorder:
            if value < lower:
                return False
            while stack and value > stack[-1]:
                lower = stack.pop()
            stack.append(value)
        return True
