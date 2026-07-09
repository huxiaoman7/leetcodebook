#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 3:45 PM
# @Author  : huxiaoman
# @File    : 234_PalindromeLinkedList.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        values = []
        while head:
            values.append(head.val)
            head = head.next
        return values == values[::-1]
