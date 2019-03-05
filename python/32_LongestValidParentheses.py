#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/28 4:52 PM
# @Author  : huxiaoman
# @File    : 32_LongestValidParentheses.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        result=0
        stk=[]
        lst=-1
        for i in xrange(len(s)):
            if s[i] == '(':
                if lst!=-1:
                    stk.append(lst)
                    lst=-1
                else:
                    stk.append(i)
            else:
                if stk:
                    stt=stk.pop()
                    if i-stt+1>result:
                        result=i-stt+1
                    lst=stt
                else:
                    lst=-1
        return result



if __name__=='__main__':
    s = Solution()
    print s.longestValidParentheses("(()()")