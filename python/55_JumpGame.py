#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/3 11:40 AM
# @Author  : huxiaoman
# @File    : 55_JumpGame.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        reach = 0
        for i, num in enumerate(nums):
            if i > reach:
                return False
            reach = max(reach, i + num)
        return True
