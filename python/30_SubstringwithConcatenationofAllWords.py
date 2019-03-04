#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/28 4:50 PM
# @Author  : huxiaoman
# @File    : 30_SubstringwithConcatenationofAllWords.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com

import collections
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:return []
        word_len = len(words[0])
        word_total = (len(words)-1) * word_len
        ans=[]
        word_cnt = collections.Counter(words)
        for i in range(word_len):
            start = i
            cur_cnt = collections.Counter()
            for j in range(i,len(s)-word_len+1, word_len):
                word = s[j:j+word_len]
                if word in word_cnt:
                    cur_cnt[word] +=1
                    while cur_cnt[word] >word_cnt[word]:
                        cur_cnt[s[start:start+word_len]] -=1
                        start += word_len
                else:
                    cur_cnt.clear()
                    start = j+word_len

                if(start+word_total == j):
                    ans.append(start)
        return ans

if __name__=="__main__":
    s = Solution()
    print s.findSubstring("barfoothefoobarman",["foo","bar"])