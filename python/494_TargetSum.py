#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/4 2:41 PM
# @Author  : huxiaoman
# @File    : 494_TargetSum.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com

class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if not nums:
            return 0
        dic = {nums[0]: 1, -nums[0]: 1} if nums[0] != 0 else {0: 2}
        print dic
        for i in range(1, len(nums)):
            tdic = {}
            for d in dic:
                tdic[d + nums[i]] = tdic.get(d + nums[i], 0) + dic.get(d, 0)
                tdic[d - nums[i]] = tdic.get(d - nums[i], 0) + dic.get(d, 0)
            dic = tdic
        return dic.get(S, 0)

if __name__=='__main__':
    s = Solution()
    print s.findTargetSumWays([1,1,1,1,1],3)