#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 5:05 PM
# @Author  : huxiaoman
# @File    : 251_Flatten2DVector.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Vector2D(object):

    def __init__(self, vec2d):
        """
        :type vec2d: List[List[int]]
        """
        self.vec2d = vec2d
        self.row = 0
        self.col = 0

    def next(self):
        """
        :rtype: int
        """
        self.move_to_next()
        value = self.vec2d[self.row][self.col]
        self.col += 1
        return value

    def hasNext(self):
        """
        :rtype: bool
        """
        self.move_to_next()
        return self.row < len(self.vec2d)

    def move_to_next(self):
        while self.row < len(self.vec2d) and self.col == len(self.vec2d[self.row]):
            self.row += 1
            self.col = 0
