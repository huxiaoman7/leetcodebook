#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 10:30 PM
# @Author  : huxiaoman
# @File    : 317_ShortestDistancefromAllBuildings.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


from collections import deque


class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return -1
        m, n = len(grid), len(grid[0])
        distance = [[0] * n for _ in range(m)]
        reach = [[0] * n for _ in range(m)]
        buildings = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    buildings += 1
                    self.bfs(grid, i, j, distance, reach)

        result = min([distance[i][j] for i in range(m) for j in range(n) if grid[i][j] == 0 and reach[i][j] == buildings] or [float('inf')])
        return -1 if result == float('inf') else result

    def bfs(self, grid, row, col, distance, reach):
        queue = deque([(row, col, 0)])
        visited = {(row, col)}
        while queue:
            i, j, dist = queue.popleft()
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and (x, y) not in visited and grid[x][y] == 0:
                    visited.add((x, y))
                    distance[x][y] += dist + 1
                    reach[x][y] += 1
                    queue.append((x, y, dist + 1))
