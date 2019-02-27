#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/27 2:26 PM
# @Author  : huxiaoman
# @File    : 1_TwoSum.py
# @Package : LeetCode

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return False
        keys = {}
        for i, v in enumerate(nums):
            if target-v in keys:
                return [keys[target-v],i]
            else:
                keys[v] = i

if __name__ == '__main__':
    s = Solution()
    print s.twoSum([2,7,11,15],9)