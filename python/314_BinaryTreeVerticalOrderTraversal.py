#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 10:15 PM
# @Author  : huxiaoman
# @File    : 314_BinaryTreeVerticalOrderTraversal.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


from collections import defaultdict, deque


class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        columns = defaultdict(list)
        queue = deque([(root, 0)])
        while queue:
            node, col = queue.popleft()
            columns[col].append(node.val)
            if node.left:
                queue.append((node.left, col - 1))
            if node.right:
                queue.append((node.right, col + 1))
        return [columns[col] for col in range(min(columns), max(columns) + 1)]
