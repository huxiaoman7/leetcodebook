#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 7:30 PM
# @Author  : huxiaoman
# @File    : 281_ZigzagIterator.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


from collections import deque


class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        :type v1: List[int]
        :type v2: List[int]
        """
        self.queue = deque()
        if v1:
            self.queue.append((v1, 0))
        if v2:
            self.queue.append((v2, 0))

    def next(self):
        """
        :rtype: int
        """
        nums, index = self.queue.popleft()
        value = nums[index]
        if index + 1 < len(nums):
            self.queue.append((nums, index + 1))
        return value

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.queue) > 0
