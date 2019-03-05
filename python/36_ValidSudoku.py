#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/28 4:54 PM
# @Author  : huxiaoman
# @File    : 36_ValidSudoku.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com

class Solution1(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        ## 方法一：按照三个规则全部检查一遍
        for i in range(9):
            if not self.isValidNine(board[i]):
                return False
            col = [c[i] for c in board]
            if not self.isValidNine(col):
                return False

        for i in [0,3,6]:
            for j in [0,3,6]:
                block = [board[s][t] for s in [i,i+1,i+2] for t in [j,j+1,j+2]]
                if not self.isValidNine(block):
                    return False
        return True

    def isValidNine(self,row):
        map = {}
        for c in row:
            if c!= '.':
                if c in map:
                    return False
                else:
                    map[c] = True
        return True

# 方法二：用三个矩阵来分别检查三个规则是否有重复数字，譬如row、col、block分别检查行、列、块是否有重复数字
class Solution2(object):
    def isValidSudoku(self,board):
        row = [[False for i in range(9)] for j in range(9)]
        col = [[False for i in range(9)] for j in range(9)]
        block = [[False for i in range(9)] for j in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j])-1
                    k=i/3*3 +j/3
                    if row[i][num] or col[j][num] or block[k][num]:
                        return False
                    row[i][num] = col[j][num] =block[k][num] =True
        return True


# 方法三：记录所有出现过的行、列、块的数字及相应的位置，最后判断是否有重复。用set操作精简代码
class Solution3(object):
    def isValidSudoku(self,board):
        seen=[]
        for i,row in enumerate(board):
            for j,c in enumerate(row):
                # print j,c
                if c !='.':
                    seen += [(c,j),(i,c),(i/3,j/3,c)]
        # print seen
        return len(seen) == len(set(seen))






if __name__=='__main__':
    s = Solution3()
    print s.isValidSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])