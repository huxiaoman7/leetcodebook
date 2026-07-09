#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 4:00 PM
# @Author  : huxiaoman
# @File    : 237_DeleteNodeinaLinkedList.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: None
        """
        node.val = node.next.val
        node.next = node.next.next
