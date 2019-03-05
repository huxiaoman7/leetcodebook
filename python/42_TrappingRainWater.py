#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/28 4:57 PM
# @Author  : huxiaoman
# @File    : 42_TrappingRainWater.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com

class Solution:
    # @param {integer[]} height
    # @return {integer}
    def trap(self, height):
        n = len(height)
        l, r, water, minHeight = 0, n - 1, 0, 0
        while l < r:
            while l < r and height[l] <= minHeight:
                water += minHeight - height[l]
                l += 1
            while r > l and height[r] <= minHeight:
                water += minHeight - height[r]
                r -= 1
            minHeight = min(height[l], height[r])
        return water



if __name__=='__main__':
    s = Solution()
    print s.trap([0,1,0,2,1,0,1,3,2,1,2,1])