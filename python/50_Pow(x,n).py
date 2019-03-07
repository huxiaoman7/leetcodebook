#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/28 5:01 PM
# @Author  : huxiaoman
# @File    : 50_Pow(x,n).py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com

class Solution:
    def myPow(self, a, b):
        if b == 0: return 1
        if b < 0: return 1.0 / self.myPow(a, -b)
        half = self.myPow(a, b // 2)
        if b % 2 == 0:
            return half * half
        else:
            return half * half * a



if __name__=='__main__':
    s = Solution()
    print s.myPow(2.00000,10)