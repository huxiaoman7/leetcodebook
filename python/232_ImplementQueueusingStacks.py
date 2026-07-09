#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/3 10:40 AM
# @Author  : huxiaoman
# @File    : 232_ImplementQueueusingStacks.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.in_stack = []
        self.out_stack = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.in_stack.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        self.peek()
        return self.out_stack.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not self.in_stack and not self.out_stack
