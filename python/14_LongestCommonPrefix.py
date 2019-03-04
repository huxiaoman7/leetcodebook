#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/28 3:37 PM
# @Author  : huxiaoman
# @File    : 14_LongestCommonPrefix.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


# 常规解法
class Solution1(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if not strs:
            return ''
        res=''
        for i in xrange(len(strs[0])):
            for j in xrange(1,len(strs)):
                if i >=len(strs[j]) or strs[j][i] !=strs[0][i]:
                    return res
            res += strs[0][i]
        print res
        return res


# 非常直观的一个解法,以最小的str去一一比对
class Solution2(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        shortest = min(strs,key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest

if __name__ == '__main__':
    s = Solution2()
    print s.longestCommonPrefix(['flower','flight','floor'])