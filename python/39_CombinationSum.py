#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/28 4:55 PM
# @Author  : huxiaoman
# @File    : 39_CombinationSum.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 方法一：DFS
        self.resList = []
        candidates = sorted(candidates)
        self.dfs(candidates,[],target,0)
        return self.resList

    def dfs(self,candidates,sublist,target,last):
        if target == 0:
            self.resList.append(sublist[:])
        if target < candidates[0]:
            return
        for n in candidates:
            if n >target:
                return
            if n<last:
                continue
            sublist.append(n)
            self.dfs(candidates,sublist,target-n,n)
            sublist.pop()







if __name__=='__main__':
    s = Solution()
    print s.combinationSum([2,3,6,7],7)