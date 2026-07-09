#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 3:05 PM
# @Author  : huxiaoman
# @File    : 225_ImplementStackusingQueues.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class MyStack(object):

    def __init__(self):
        self.queue = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue.append(x)
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.pop(0))

    def pop(self):
        """
        :rtype: int
        """
        return self.queue.pop(0)

    def top(self):
        """
        :rtype: int
        """
        return self.queue[0]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.queue
