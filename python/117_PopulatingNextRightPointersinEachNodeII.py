#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/6 12:40 PM
# @Author  : huxiaoman
# @File    : 117_PopulatingNextRightPointersinEachNodeII.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        cur = root
        while cur:
            dummy = type(cur)(0)
            tail = dummy
            while cur:
                if cur.left:
                    tail.next = cur.left
                    tail = tail.next
                if cur.right:
                    tail.next = cur.right
                    tail = tail.next
                cur = cur.next
            cur = dummy.next
        return root
