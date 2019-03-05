#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/28 4:56 PM
# @Author  : huxiaoman
# @File    : 40_CombinationSumII.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        #方法一：DFS
        candidates.sort()
        print candidates
        res=[]
        self.dfs(candidates, target, 0, res, [])
        return res

    def dfs(self, nums, target,index,res,path):
        if target < 0:
            return
        elif target == 0:
            res.append(path)
            return
        for i in xrange(index, len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
            self.dfs(nums,target-nums[i],i+1,res,path+[nums[i]])







if __name__=='__main__':
    s = Solution()
    print s.combinationSum2([10,1,2,7,6,1,5],8)