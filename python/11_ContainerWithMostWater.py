#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/28 3:37 PM
# @Author  : huxiaoman
# @File    : 11_ContainerWithMostWater.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


# two pointers
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area = 0
        l = 0
        r = len(height)-1

        while l < r:
            area = max(area,min(height[l],height[r])*(r-l))
            if height[r] > height[l]:
                l += 1
            else:
                r -=1
        return area



if __name__ == '__main__':
    s = Solution()
    print s.maxArea([1,1,3,4,5])
