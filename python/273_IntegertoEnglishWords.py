#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 6:50 PM
# @Author  : huxiaoman
# @File    : 273_IntegertoEnglishWords.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return 'Zero'

        units = ['', 'Thousand', 'Million', 'Billion']
        words = []
        index = 0
        while num:
            part = num % 1000
            if part:
                chunk = self.convert(part)
                if units[index]:
                    chunk.append(units[index])
                words = chunk + words
            num //= 1000
            index += 1
        return ' '.join(words)

    def convert(self, num):
        below_20 = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
                    'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen',
                    'Seventeen', 'Eighteen', 'Nineteen']
        tens = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        result = []
        if num >= 100:
            result.extend([below_20[num // 100], 'Hundred'])
            num %= 100
        if num >= 20:
            result.append(tens[num // 10])
            num %= 10
        if num > 0:
            result.append(below_20[num])
        return result
