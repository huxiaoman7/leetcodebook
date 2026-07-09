#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/6 12:30 PM
# @Author  : huxiaoman
# @File    : 116_PopulatingNextRightPointersinEachNode.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if not root:
            return root
        leftmost = root
        while leftmost.left:
            cur = leftmost
            while cur:
                cur.left.next = cur.right
                if cur.next:
                    cur.right.next = cur.next.left
                cur = cur.next
            leftmost = leftmost.left
        return root
