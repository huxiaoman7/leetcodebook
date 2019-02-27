#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/27 2:28 PM
# @Author  : huxiaoman
# @File    : 2_Add_Two_Sum_Numbers.py
# @Package : LeetCode

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self,l1,l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        answer = head
        carry = 0
        while l1 and l2:
            add = l1.val + l2.val + carry
            carry = 1 if add >=10 else 0
            head.next = ListNode(add % 10)
            head = head.next
            l1,l2 = l1.next,l2.next

        l = l1 if l2 else l2
        while l:
            add = l.val+carry
            carry = 1 if add >= 10 else 0
            head.next = ListNode(add %10)
            head = head.next

        if carry:
            head.next = ListNode(1)
        return answer.next






