#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 12:55 AM
# @Author  : huxiaoman
# @File    : 346_MovingAveragefromDataStream.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


from collections import deque


class MovingAverage(object):

    def __init__(self, size):
        """
        :type size: int
        """
        self.size = size
        self.queue = deque()
        self.total = 0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.queue.append(val)
        self.total += val
        if len(self.queue) > self.size:
            self.total -= self.queue.popleft()
        return float(self.total) / len(self.queue)
