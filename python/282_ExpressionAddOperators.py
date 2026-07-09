#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 7:35 PM
# @Author  : huxiaoman
# @File    : 282_ExpressionAddOperators.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        result = []
        self.dfs(num, target, 0, 0, 0, '', result)
        return result

    def dfs(self, num, target, index, value, last, path, result):
        if index == len(num):
            if value == target:
                result.append(path)
            return

        for i in range(index, len(num)):
            if i != index and num[index] == '0':
                break
            current = int(num[index:i + 1])
            current_string = num[index:i + 1]
            if index == 0:
                self.dfs(num, target, i + 1, current, current, current_string, result)
            else:
                self.dfs(num, target, i + 1, value + current, current, path + '+' + current_string, result)
                self.dfs(num, target, i + 1, value - current, -current, path + '-' + current_string, result)
                self.dfs(num, target, i + 1, value - last + last * current, last * current, path + '*' + current_string, result)
