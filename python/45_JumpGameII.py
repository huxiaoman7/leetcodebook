#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/28 4:58 PM
# @Author  : huxiaoman
# @File    : 45_JumpGameII.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n, start, end, step = len(nums), 0, 0, 0
        while end < n - 1:
            step += 1
            maxend = end + 1
            for i in range(start, end + 1):
                if i + nums[i] >= n - 1:
                    return step
                maxend = max(maxend, i + nums[i])
            start, end = end + 1, maxend
        return step




if __name__=='__main__':
    s = Solution()
    print s.jump([2,3,1,1,4])