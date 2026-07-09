#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 1:30 AM
# @Author  : huxiaoman
# @File    : 353_DesignSnakeGame.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


from collections import deque


class SnakeGame(object):

    def __init__(self, width, height, food):
        """
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        self.width = width
        self.height = height
        self.food = food
        self.food_index = 0
        self.snake = deque([(0, 0)])
        self.body = {(0, 0)}
        self.moves = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

    def move(self, direction):
        """
        :type direction: str
        :rtype: int
        """
        head_r, head_c = self.snake[0]
        dr, dc = self.moves[direction]
        new_head = (head_r + dr, head_c + dc)
        tail = self.snake.pop()
        self.body.remove(tail)
        if (new_head[0] < 0 or new_head[0] >= self.height or
                new_head[1] < 0 or new_head[1] >= self.width or new_head in self.body):
            return -1
        self.snake.appendleft(new_head)
        self.body.add(new_head)
        if self.food_index < len(self.food) and list(new_head) == self.food[self.food_index]:
            self.snake.append(tail)
            self.body.add(tail)
            self.food_index += 1
        return self.food_index
