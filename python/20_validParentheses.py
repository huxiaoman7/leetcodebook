#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/28 3:55 PM
# @Author  : huxiaoman
# @File    : 20_validParentheses.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pars = [None]
        #这个字典建立的顺序也很重要
        parmap = {')':'(','}':'{',']':'['}
        for c in s:
            if c in parmap:
                if parmap[c] !=pars.pop():
                    return False
            else:
                pars.append(c)
        return len(pars) == 1

if __name__=='__main__':
    s = Solution()
    print s.isValid(")(")