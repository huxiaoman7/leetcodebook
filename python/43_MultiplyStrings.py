#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/28 4:57 PM
# @Author  : huxiaoman
# @File    : 43_MultiplyStrings.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        n1=0
        i=0
        for x in num1[::-1]:
            n1=n1+(ord(x)-ord('0'))*(10**i)
            i+=1
        r=0
        i=0
        for y in num2[::-1]:
            r=r+n1*((ord(y)-ord('0'))*10**i)
            i+=1
        return str(r)


if __name__=='__main__':
    s = Solution()
    print s.multiply("2","3")