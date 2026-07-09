#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 5:15 PM
# @Author  : huxiaoman
# @File    : 253_MeetingRoomsII.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


import heapq


class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals:
            return 0
        intervals.sort()
        rooms = []
        for start, end in intervals:
            if rooms and rooms[0] <= start:
                heapq.heappop(rooms)
            heapq.heappush(rooms, end)
        return len(rooms)
