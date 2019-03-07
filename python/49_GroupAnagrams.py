#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/28 5:00 PM
# @Author  : huxiaoman
# @File    : 49_GroupAnagrams.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # strs.sort()
        d = {}
        for str in strs:
            s = "".join(sorted(str))
            if s not in d:
                d[s] = [str]#为什么这里要加[]
            else:
                d[s].append(str)
        res = []
        for k, v in d.items():
            res.append(v)
        return res


if __name__=='__main__':
    s = Solution()
    print s.groupAnagrams(["eat","tea","tan","ate","nat","bat"])