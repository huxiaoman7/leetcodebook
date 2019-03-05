#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/28 4:52 PM
# @Author  : huxiaoman
# @File    : 31_NextPermutation.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        for x in range(size - 1, -1, -1):
            if nums[x - 1] < nums[x]:
                break
        if x > 0:
            for y in range(size - 1, -1, -1):
                if nums[y] > nums[x - 1]:
                    nums[x - 1], nums[y] = nums[y], nums[x - 1]
                    break
        for z in range((size - x) / 2):
            nums[x + z], nums[size - z - 1] = nums[size - z - 1], nums[x + z]

if __name__=='__main__':
    s = Solution()
    print s.nextPermutation([1,2,3])
