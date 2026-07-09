#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 1:55 AM
# @Author  : huxiaoman
# @File    : 358_RearrangeStringkDistanceApart.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


from collections import Counter, deque
import heapq


class Solution(object):
    def rearrangeString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if k <= 1:
            return s
        heap = [(-count, ch) for ch, count in Counter(s).items()]
        heapq.heapify(heap)
        wait = deque()
        result = []
        while len(result) < len(s):
            while wait and wait[0][0] <= len(result):
                _, count, ch = wait.popleft()
                heapq.heappush(heap, (count, ch))
            if not heap:
                return ''
            count, ch = heapq.heappop(heap)
            result.append(ch)
            if count + 1 < 0:
                wait.append((len(result) - 1 + k, count + 1, ch))
        return ''.join(result)
