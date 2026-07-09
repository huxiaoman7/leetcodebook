#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/5 11:40 AM
# @Author  : huxiaoman
# @File    : 92_ReverseLinkedListII.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head or m == n:
            return head
        dummy = type(head)(0)
        dummy.next = head
        prev = dummy
        for _ in range(m - 1):
            prev = prev.next
        cur = prev.next
        for _ in range(n - m):
            nxt = cur.next
            cur.next = nxt.next
            nxt.next = prev.next
            prev.next = nxt
        return dummy.next
