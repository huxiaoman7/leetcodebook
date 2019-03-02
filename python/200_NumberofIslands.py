#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/2 10:28 AM
# @Author  : huxiaoman
# @File    : 200_NumberofIslands.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com

# DFS
# time:O(M*N) space:O(M*N) assume the matrix[N][N]
class Solution(object):
    def numIslands(self,grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        island = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid,i,j)
                    island += 1
        return island

    def dfs(self,grid,i,j):
        #corner case
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] !=  '1':
            return 0
        # visited ='*'
        grid[i][j] = '*'
        self.dfs(grid, i+1,j)
        self.dfs(grid, i-1,j)
        self.dfs(grid, i,j+1)
        self.dfs(grid, i,j-1)


if __name__ == '__main__':
    s = Solution()
    print s.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])