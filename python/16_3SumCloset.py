#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/28 3:44 PM
# @Author  : huxiaoman
# @File    : 16_3SumCloset.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com

import itertools
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        minval = 100000
        nums.sort()
        for i in range(len(nums)):
            left = i+1
            right = len(nums)-1
            while left<right:
                val=nums[i]+nums[left]+nums[right]
                if abs(val-target) <minval:
                    minval = abs(val-target)
                    result = val
                if val == target:
                    return target
                if val <= target:
                    left +=1
                else:
                    right -= 1
        return result


if __name__=='__main__':
    s = Solution()
    print s.threeSumClosest([-1,2,1,-4],1)