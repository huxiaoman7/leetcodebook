#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/4 11:10 AM
# @Author  : huxiaoman
# @File    : 68_TextJustification.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        result = []
        i = 0
        while i < len(words):
            line_len = len(words[i])
            j = i + 1
            while j < len(words) and line_len + 1 + len(words[j]) <= maxWidth:
                line_len += 1 + len(words[j])
                j += 1

            count = j - i
            if j == len(words) or count == 1:
                line = ' '.join(words[i:j])
                result.append(line + ' ' * (maxWidth - len(line)))
            else:
                words_len = sum(len(word) for word in words[i:j])
                spaces = maxWidth - words_len
                gap = count - 1
                even = spaces // gap
                extra = spaces % gap
                line = ''
                for k in range(i, j - 1):
                    line += words[k]
                    line += ' ' * (even + (1 if k - i < extra else 0))
                line += words[j - 1]
                result.append(line)
            i = j
        return result
