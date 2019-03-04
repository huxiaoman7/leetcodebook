#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/28 4:49 PM
# @Author  : huxiaoman
# @File    : 29_DivideTwoIntegers.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        #二分查找
        sign = 1
        if (dividend > 0 and divisor < 0) or (dividend <0 and divisor > 0):
            sign = -1
            if abs(dividend) < abs(divisor):
                return 0
        res = 0
        a = abs(dividend)
        b = abs(divisor)
        sum = 0
        count = 0
        while a>=b:
            sum=b
            count=1
            while sum+sum <=a:
                sum+=sum
                count +=count
            a-=sum
            res +=count
        if sign == -1:
            res=0-res
        if res >=pow(2,31)-1 and sign ==1:return pow(2,31) -1
        if res >=pow(2,31) and sign == -1:return -pow(2,31)
        return res

if __name__=='__main__':
    s = Solution()
    print s.divide(10,3)