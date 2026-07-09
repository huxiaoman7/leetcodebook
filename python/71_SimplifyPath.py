#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/4 11:40 AM
# @Author  : huxiaoman
# @File    : 71_SimplifyPath.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        for part in path.split('/'):
            if part == '' or part == '.':
                continue
            if part == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(part)
        return '/' + '/'.join(stack)
