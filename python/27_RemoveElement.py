#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/28 4:49 PM
# @Author  : huxiaoman
# @File    : 27_RemoveElement.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # 方法一：用两个指针，一个指针顺序扫描素有元素判断当前元素是否需要删除，另一个指针一直指向下一个不是要删除元素的位置
        # 这样相当于把原数组中要删除的数去除后，所有其他数字前移

        length = 0

        for i in xrange(len(nums)):
            if nums[i] !=val:
                nums[length] =nums[i]
                length += 1
        return length

if __name__=='__main__':
    s = Solution()
    print s.removeElement([2,3,3,2],3)