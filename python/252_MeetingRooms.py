#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 5:10 PM
# @Author  : huxiaoman
# @File    : 252_MeetingRooms.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        intervals.sort()
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i - 1][1]:
                return False
        return True
