#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/28 4:58 PM
# @Author  : huxiaoman
# @File    : 46_Permutations.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
            # return # backtracking
        for i in xrange(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)



if __name__=='__main__':
    s = Solution()
    print s.permute([1,2,3])