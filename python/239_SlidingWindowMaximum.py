#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/3 10:50 AM
# @Author  : huxiaoman
# @File    : 239_SlidingWindowMaximum.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


from collections import deque


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums or k <= 0:
            return []
        queue = deque()
        result = []
        for i, num in enumerate(nums):
            if queue and queue[0] <= i - k:
                queue.popleft()
            while queue and nums[queue[-1]] <= num:
                queue.pop()
            queue.append(i)
            if i >= k - 1:
                result.append(nums[queue[0]])
        return result
