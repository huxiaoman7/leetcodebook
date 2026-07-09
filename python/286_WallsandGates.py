#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 7:55 PM
# @Author  : huxiaoman
# @File    : 286_WallsandGates.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


from collections import deque


class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not rooms[0]:
            return
        queue = deque()
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    queue.append((i, j))

        while queue:
            i, j = queue.popleft()
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < len(rooms) and 0 <= y < len(rooms[0]) and rooms[x][y] == 2147483647:
                    rooms[x][y] = rooms[i][j] + 1
                    queue.append((x, y))
