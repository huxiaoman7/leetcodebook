#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 2:40 AM
# @Author  : huxiaoman
# @File    : 369_PlusOneLinkedList.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):

    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = type(head)(0)
        dummy.next = head
        last_not_nine = dummy
        current = head
        while current:
            if current.val != 9:
                last_not_nine = current
            current = current.next
        last_not_nine.val += 1
        current = last_not_nine.next
        while current:
            current.val = 0
            current = current.next
        return dummy if dummy.val else dummy.next
