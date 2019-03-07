#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/28 5:00 PM
# @Author  : huxiaoman
# @File    : 47_PermutationsII.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        ans = [[]]
        for n in nums:
            new_ans = []
            for l in ans:
                for i in xrange(len(l)+1):
                    new_ans.append(l[:i]+[n]+l[i:])
                    if i<len(l) and l[i]==n: break
            ans = new_ans
        return ans




if __name__=='__main__':
    s = Solution()
    print s.permuteUnique([1,1,2])