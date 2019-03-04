#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/28 3:48 PM
# @Author  : huxiaoman
# @File    : 19_RemoveNthNodeFromEndofList.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        new_head = ListNode(0)
        new_head.next =head
        fast=slow=new_head
        for i in range(n+1):
            fast = fast.next
        while fast:
            fast=fast.next
            slow=slow.next
        slow.next=slow.next.next
        return new_head.next


if __name__=='__main__':
    s = Solution()
    print  s.removeNthFromEnd([1,2,3,4,5],2)