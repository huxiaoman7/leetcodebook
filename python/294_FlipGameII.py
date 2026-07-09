#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 8:35 PM
# @Author  : huxiaoman
# @File    : 294_FlipGameII.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def canWin(self, currentState):
        """
        :type currentState: str
        :rtype: bool
        """
        memo = {}
        return self.dfs(currentState, memo)

    def dfs(self, state, memo):
        if state in memo:
            return memo[state]
        for i in range(len(state) - 1):
            if state[i:i + 2] == '++':
                nxt = state[:i] + '--' + state[i + 2:]
                if not self.dfs(nxt, memo):
                    memo[state] = True
                    return True
        memo[state] = False
        return False
