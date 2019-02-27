#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/27 2:30 PM
# @Author  : huxiaoman
# @File    : 3_longest_substring_without_repeating_characters.py
# @Package : LeetCode


class Solution:
    """
    :type s: str
    :rtype: int
    """
    def lengthOfLongestSubstring(self, s):
        max_length, start, char_dict = 0, 0, {}
        for idx, char in enumerate(s, 1):
            if char_dict.get(char, -1) >= start:
                start = char_dict[char]
            char_dict[char] = idx
            max_length = max(max_length, idx - start)
        return max_length

if __name__ == '__main__':
    s = Solution()
    print s.lengthOfLongestSubstring("abcabcbb")