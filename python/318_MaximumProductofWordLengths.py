#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 10:35 PM
# @Author  : huxiaoman
# @File    : 318_MaximumProductofWordLengths.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        masks = []
        for word in words:
            mask = 0
            for ch in set(word):
                mask |= 1 << (ord(ch) - ord('a'))
            masks.append((mask, len(word)))

        result = 0
        for i in range(len(masks)):
            for j in range(i + 1, len(masks)):
                if masks[i][0] & masks[j][0] == 0:
                    result = max(result, masks[i][1] * masks[j][1])
        return result
