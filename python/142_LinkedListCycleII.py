#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/8 10:10 AM
# @Author  : huxiaoman
# @File    : 142_LinkedListCycleII.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                cur = head
                while cur is not slow:
                    cur = cur.next
                    slow = slow.next
                return cur
        return None
