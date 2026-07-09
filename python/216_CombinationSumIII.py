#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 2:20 PM
# @Author  : huxiaoman
# @File    : 216_CombinationSumIII.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        result = []
        self.backtrack(k, n, 1, [], result)
        return result

    def backtrack(self, k, target, start, path, result):
        if len(path) == k:
            if target == 0:
                result.append(path[:])
            return
        for num in range(start, 10):
            if num > target:
                break
            path.append(num)
            self.backtrack(k, target - num, num + 1, path, result)
            path.pop()
