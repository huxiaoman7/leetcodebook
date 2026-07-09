#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 6:40 PM
# @Author  : huxiaoman
# @File    : 271_EncodeandDecodeStrings.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Codec(object):
    def encode(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        return ''.join('%s#%s' % (len(s), s) for s in strs)

    def decode(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        i = 0
        while i < len(s):
            j = s.find('#', i)
            length = int(s[i:j])
            j += 1
            result.append(s[j:j + length])
            i = j + length
        return result
