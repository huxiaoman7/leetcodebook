#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/28 4:55 PM
# @Author  : huxiaoman
# @File    : 38_CountandSay.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for _ in range(n-1):
            let, temp, count = s[0], '', 0
            for l in s:
                if let == l:
                    count += 1
                else:
                    temp += str(count)+let
                    let = l
                    count = 1
            temp += str(count)+let
            s = temp
        return s







if __name__=='__main__':
    s = Solution()
    print s.countAndSay(11)