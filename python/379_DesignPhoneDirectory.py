#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 3:30 AM
# @Author  : huxiaoman
# @File    : 379_DesignPhoneDirectory.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class PhoneDirectory(object):

    def __init__(self, maxNumbers):
        """
        :type maxNumbers: int
        """
        self.available = set(range(maxNumbers))

    def get(self):
        """
        :rtype: int
        """
        if not self.available:
            return -1
        number = min(self.available)
        self.available.remove(number)
        return number

    def check(self, number):
        """
        :type number: int
        :rtype: bool
        """
        return number in self.available

    def release(self, number):
        """
        :type number: int
        :rtype: None
        """
        self.available.add(number)
