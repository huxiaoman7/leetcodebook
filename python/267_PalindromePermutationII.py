#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 6:20 PM
# @Author  : huxiaoman
# @File    : 267_PalindromePermutationII.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


from collections import Counter


class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        counts = Counter(s)
        odd = [ch for ch, count in counts.items() if count % 2]
        if len(odd) > 1:
            return []

        middle = odd[0] if odd else ''
        half = []
        for ch, count in counts.items():
            half.extend([ch] * (count // 2))

        result = []
        self.backtrack(sorted(half), [False] * len(half), [], middle, result)
        return result

    def backtrack(self, half, used, path, middle, result):
        if len(path) == len(half):
            left = ''.join(path)
            result.append(left + middle + left[::-1])
            return
        for i, ch in enumerate(half):
            if used[i] or (i > 0 and half[i] == half[i - 1] and not used[i - 1]):
                continue
            used[i] = True
            path.append(ch)
            self.backtrack(half, used, path, middle, result)
            path.pop()
            used[i] = False
