#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/28 4:00 PM
# @Author  : huxiaoman
# @File    : 23_MergeKSortedLists.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


from Queue import PriorityQueue

class Solution(object):
    def mergeKLists(self, lists):
        dummy = ListNode(None)
        curr = dummy
        q = PriorityQueue()
        for node in lists:
            if node: q.put((node.val,node))
        while q.qsize()>0:
            curr.next = q.get()[1]
            curr=curr.next
            if curr.next: q.put((curr.next.val, curr.next))
        return dummy.next
