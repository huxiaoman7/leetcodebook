#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/28 4:56 PM
# @Author  : huxiaoman
# @File    : 41_FirstMissingPositive.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.append(0)
        n = len(nums)
        for i in range(len(nums)):
            if nums[i]<0 or nums[i]>=n:
                nums[i]=0
        for i in range(len(nums)):
            nums[nums[i]%n]+=n
        for i in range(1,len(nums)):
            if nums[i]/n==0:
                return i
        return n





if __name__=='__main__':
    s = Solution()
    print s.firstMissingPositive([1,2,0])
