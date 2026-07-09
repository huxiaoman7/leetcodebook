#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/8 12:50 PM
# @Author  : huxiaoman
# @File    : 160_IntersectionofTwoLinkedLists.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        a, b = headA, headB
        while a is not b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a
