#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 8:30 PM
# @Author  : huxiaoman
# @File    : 293_FlipGame.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def generatePossibleNextMoves(self, currentState):
        """
        :type currentState: str
        :rtype: List[str]
        """
        result = []
        for i in range(len(currentState) - 1):
            if currentState[i:i + 2] == '++':
                result.append(currentState[:i] + '--' + currentState[i + 2:])
        return result
