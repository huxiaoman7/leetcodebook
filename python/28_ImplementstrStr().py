#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/28 4:49 PM
# @Author  : huxiaoman
# @File    : 28_ImplementstrStr().py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        for i in xrange(len(haystack) - len(needle)+1):
            if haystack[i] == needle[0]:
                j = 1
                while j  < len(needle)  and haystack[i+j] ==needle[j]:
                    j+=1
                if j ==len(needle):
                    return i
        return -1

if __name__=='__main__':
    s = Solution()
    print s.strStr('hello','ll')