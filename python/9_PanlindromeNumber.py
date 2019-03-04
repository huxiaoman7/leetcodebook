#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/28 3:34 PM
# @Author  : huxiaoman
# @File    : 9_PanlindromeNumber.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        elif x>=0 :
            if str(x) == str(x)[::-1]:
                return True
            else:
                return False

if __name__ =='__main__':
    s = Solution()
    print s.isPalindrome(32123)