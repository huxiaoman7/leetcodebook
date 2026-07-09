#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 1:20 PM
# @Author  : huxiaoman
# @File    : 203_RemoveLinkedListElements.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return None
        dummy = head.__class__(0)
        dummy.next = head
        current = dummy
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        return dummy.next
