#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 8:45 PM
# @Author  : huxiaoman
# @File    : 296_BestMeetingPoint.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = []
        cols = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    rows.append(i)
                    cols.append(j)
        cols.sort()
        return self.distance(rows) + self.distance(cols)

    def distance(self, nums):
        total = 0
        left, right = 0, len(nums) - 1
        while left < right:
            total += nums[right] - nums[left]
            left += 1
            right -= 1
        return total
