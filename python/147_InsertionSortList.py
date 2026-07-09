#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/8 11:00 AM
# @Author  : huxiaoman
# @File    : 147_InsertionSortList.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        dummy = type(head)(0)
        cur = head
        while cur:
            nxt = cur.next
            pos = dummy
            while pos.next and pos.next.val < cur.val:
                pos = pos.next
            cur.next = pos.next
            pos.next = cur
            cur = nxt
        return dummy.next
