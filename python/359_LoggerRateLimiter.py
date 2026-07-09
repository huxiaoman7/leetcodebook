#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 2:00 AM
# @Author  : huxiaoman
# @File    : 359_LoggerRateLimiter.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Logger(object):

    def __init__(self):
        self.next_time = {}

    def shouldPrintMessage(self, timestamp, message):
        """
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if timestamp >= self.next_time.get(message, 0):
            self.next_time[message] = timestamp + 10
            return True
        return False
