#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/28 3:47 PM
# @Author  : huxiaoman
# @File    : 17_LetterCombinationsofaPhoneNumbr.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com

class Solution:
    """
    :type digits: str
    :rtype: List[str]
    """
    def letterCombinations(self, digits):
        phonedict = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return list(phonedict[digits[0]])
        prev = self.letterCombinations(digits[:-1])
        additional = phonedict[digits[-1]]
        return [s + c for s in prev for c in additional]

if __name__ =='__main__':
    s = Solution()
    print s.letterCombinations("23")