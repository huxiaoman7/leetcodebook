#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/28 3:34 PM
# @Author  : huxiaoman
# @File    : 8_StringToInteger(aoti).py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com

import re

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        try:
            res = re.search('(^[\+\-]?\d+)', str).group()
            res = int(res)
            res = res if res <= 2147483647 else 2147483647
            res = res if res >= -2147483648 else -2147483648
        except:
            res = 0
        return res

if __name__ == '__main__':
    s = Solution()
    print s.myAtoi("4232")