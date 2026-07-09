#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/4 10:00 AM
# @Author  : huxiaoman
# @File    : 61_RotateList.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next or k == 0:
            return head
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        k %= length
        if k == 0:
            return head

        tail.next = head
        steps = length - k
        new_tail = tail
        while steps:
            new_tail = new_tail.next
            steps -= 1
        new_head = new_tail.next
        new_tail.next = None
        return new_head
