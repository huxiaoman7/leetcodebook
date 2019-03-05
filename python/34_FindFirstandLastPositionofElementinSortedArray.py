#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/28 4:54 PM
# @Author  : huxiaoman
# @File    : 34_FindFirstandLastPositionofElementinSortedArray.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution:

    def searchRange(self, nums, target):
        left_idx = self.extreme_insertion_index(nums, target, True)

        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1, -1]

        return [left_idx, self.extreme_insertion_index(nums, target, False)-1]


    def extreme_insertion_index(self, nums, target, left):
        lo = 0
        hi = len(nums)

        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > target or (left and target == nums[mid]):
                hi = mid
            else:
                lo = mid+1

        return lo



if __name__=='__main__':
    s = Solution()
    print s.searchRange([5,7,7,8,8,10],8)