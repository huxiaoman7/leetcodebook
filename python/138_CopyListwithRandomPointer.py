#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/7 12:50 PM
# @Author  : huxiaoman
# @File    : 138_CopyListwithRandomPointer.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
        copies = {}
        cur = head
        while cur:
            copies[cur] = type(cur)(cur.label)
            cur = cur.next
        cur = head
        while cur:
            copies[cur].next = copies.get(cur.next)
            copies[cur].random = copies.get(cur.random)
            cur = cur.next
        return copies[head]
