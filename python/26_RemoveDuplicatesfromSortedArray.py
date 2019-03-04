#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/28 4:48 PM
# @Author  : huxiaoman
# @File    : 26_RemoveDuplicatesfromSortedArray.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com

class Solution1(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 方法一：用两个指针，一个指针用于扫描遍历整个列表，
        # 另一个指针时终止向下一个数字要写入列表的位置，
        # 效果相当于在便利列表的时候，将不同的数字重新写入到原数组

        if len(nums)==0:
            return 0
        cur=0
        for i in range(1,len(nums)):
            if nums[i] != nums[cur]:
                cur +=1
                nums[cur] = nums[i]
        return cur+1

class Solution2(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 方法二：用一个计数器记录当前有多少重复数字，
        # 以此来决定下一个要写入数组的数字的位置，
        # 以及当便利玩数组时得到的新长度
        count = 0
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                count +=1
            else:
                nums[i-count] = nums[i]
        return len(nums)-count


if __name__=='__main__':
    s = Solution2()
    print s.removeDuplicates([1,1,2])