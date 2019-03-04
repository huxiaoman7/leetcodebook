#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/28 3:33 PM
# @Author  : huxiaoman
# @File    : 5_LongestPanlindromicSubstring.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com

class Solution(object):
    """
    :type s: str
    :rtype: str
    """
    def longestPalindrome(self, s):
        res = ""
        for i in xrange(len(s)):
            tmp = self.helper(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            tmp = self.helper(s, i, i+1)
            if len(tmp) > len(res):
                res = tmp
        return res


    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        return s[l+1:r]


if __name__ == '__main__':
    s = Solution()
    print s.longestPalindrome("babad")

