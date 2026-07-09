#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 2:05 AM
# @Author  : huxiaoman
# @File    : 362_DesignHitCounter.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


from collections import deque


class HitCounter(object):

    def __init__(self):
        self.hits = deque()

    def hit(self, timestamp):
        """
        :type timestamp: int
        :rtype: None
        """
        self.hits.append(timestamp)

    def getHits(self, timestamp):
        """
        :type timestamp: int
        :rtype: int
        """
        while self.hits and self.hits[0] <= timestamp - 300:
            self.hits.popleft()
        return len(self.hits)
