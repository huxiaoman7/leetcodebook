#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/28 5:00 PM
# @Author  : huxiaoman
# @File    : 48_RotateImage.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com



class Solution1:
    def rotate(self, matrix):
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                matrix[j][i],matrix[i][j]=matrix[i][j],matrix[j][i]
        return matrix


class Solution2:
    def rotate(self,matrix):
        n = len(matrix[0])
        for i in range(n):
            for j in range(i,n):
                matrix[j][i],matrix[i][j] = matrix[i][j],matrix[j][i]

        for i in range(n):
            print matrix[i]
            matrix[i].reverse()
        return matrix

class Solution3(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        matrix[:] = [list(a) for a in zip(*matrix)]
        for row in matrix:
            row[:] = row[::-1]
        return matrix

class Solution4(object):
    def rotate(self,matrix):
        n = len(matrix[0])
        for i in range(n // 2 + n %2):
            for j in range(n // 2):
                tmp = [0] * 4;
                row ,col = i,j
                for k in range(4):
                    tmp[k] = matrix[row][col]
                    row, col = col,n-1-row

                for k in range(4):
                    matrix[row][col] = tmp[(k-1) % 4]
                    row,col = col,n-1-row
        return matrix




if __name__=='__main__':
    s = Solution3()
    print s.rotate([[1,2,3],[4,5,6],[7,8,9]])