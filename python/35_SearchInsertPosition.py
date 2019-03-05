#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/28 4:54 PM
# @Author  : huxiaoman
# @File    : 35_SearchInsertPosition.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low, high = 0, len(nums)
        while low < high:
            mid = (low+high)/2
            if nums[mid] >= target:
                high = mid
            else:
                low = mid + 1
        return low


if __name__=='__main__':
    s = Solution()
    print s.searchInsert([1,3,5,6],5)