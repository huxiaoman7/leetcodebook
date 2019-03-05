#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/28 4:53 PM
# @Author  : huxiaoman
# @File    : 33_SearchinRotatedSortedArray.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums)-1

        while start <= end:
            mid = (start+end)/2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[start]:
                if target >= nums[start] and target<nums[mid]:
                    end = mid-1
                else:
                    start = mid+1

            if nums[mid] <nums[end]:
                if target>nums[mid] and target<=nums[end]:
                    start = mid+1
                else:
                    end=mid-1

        return -1






if __name__=='__main__':
    s = Solution()
    print s.search([4,5,6,7,0,1,2],0)