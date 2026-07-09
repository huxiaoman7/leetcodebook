#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/5 10:40 AM
# @Author  : huxiaoman
# @File    : 86_PartitionList.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return head
        small_dummy = type(head)(0)
        large_dummy = type(head)(0)
        small = small_dummy
        large = large_dummy
        while head:
            nxt = head.next
            head.next = None
            if head.val < x:
                small.next = head
                small = small.next
            else:
                large.next = head
                large = large.next
            head = nxt
        small.next = large_dummy.next
        return small_dummy.next
