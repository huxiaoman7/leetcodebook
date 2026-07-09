#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/3 10:30 AM
# @Author  : huxiaoman
# @File    : 207_CourseSchedule.py
# @Package : LeetCode
# @E-mail  : charlotte77_hu@sina.com


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1

        queue = [i for i in range(numCourses) if indegree[i] == 0]
        count = 0
        for node in queue:
            count += 1
            for nxt in graph[node]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)
        return count == numCourses
