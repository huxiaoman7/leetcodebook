#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/27 6:01 PM
# @Author  : huxiaoman
# @File    : 4_MedianofTwoSortedArray.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com

# 二分+递归:同找到数组中第K个最大的元素相同,这里是两个数组,所以分别找到两个数组的第k个最大的元素,然后求均值
class Solution(object):
    def findMedianSortedArrays(self, A, B):
        l = len(A) + len(B)
        if l % 2 == 1:
            return self.findkth(A, B, l // 2)
        else:
            return (self.findkth(A, B, l // 2) + self.findkth(A, B, l // 2 - 1)) / 2.

    def findkth(self, a, b, k):
        if not a:
            return b[k]
        if not b:
            return a[k]
        ia, ib = len(a) // 2 , len(b) // 2
        ma, mb = a[ia], b[ib]

        if ia + ib < k:
            if ma > mb:
                return self.findkth(a, b[ib + 1:], k - ib - 1)
            else:
                return self.findkth(a[ia + 1:], b, k - ia - 1)
        else:
            if ma > mb:
                return self.findkth(a[:ia], b, k)
            else:
                return self.findkth(a, b[:ib], k)

if __name__ == '__main__':
    s = Solution()
    print s.findMedianSortedArrays([1,2,3,4,5],[6,7,8,9])

