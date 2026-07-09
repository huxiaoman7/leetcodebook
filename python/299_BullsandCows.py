#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 9:00 PM
# @Author  : huxiaoman
# @File    : 299_BullsandCows.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


from collections import Counter


class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bulls = sum(a == b for a, b in zip(secret, guess))
        both = sum((Counter(secret) & Counter(guess)).values())
        return '%sA%sB' % (bulls, both - bulls)
