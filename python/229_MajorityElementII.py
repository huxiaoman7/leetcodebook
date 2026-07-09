#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 3:25 PM
# @Author  : huxiaoman
# @File    : 229_MajorityElementII.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        candidate1, candidate2 = None, None
        count1, count2 = 0, 0
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1
        return [num for num in (candidate1, candidate2) if num is not None and nums.count(num) > len(nums) // 3]
