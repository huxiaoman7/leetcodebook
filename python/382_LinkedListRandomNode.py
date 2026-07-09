#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 3:45 AM
# @Author  : huxiaoman
# @File    : 382_LinkedListRandomNode.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


import random


class Solution(object):

    def __init__(self, head):
        """
        :type head: ListNode
        """
        self.head = head

    def getRandom(self):
        """
        :rtype: int
        """
        result = self.head.val
        current = self.head.next
        count = 2
        while current:
            if random.randrange(count) == 0:
                result = current.val
            current = current.next
            count += 1
        return result
