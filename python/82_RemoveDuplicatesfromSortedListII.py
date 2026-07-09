#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/5 10:10 AM
# @Author  : huxiaoman
# @File    : 82_RemoveDuplicatesfromSortedListII.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = type(head)(0) if head else None
        if not dummy:
            return None
        dummy.next = head
        prev = dummy
        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                prev.next = head.next
            else:
                prev = prev.next
            head = head.next
        return dummy.next
