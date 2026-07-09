# 队列知识点&题型讲解

## 知识点

### 什么是队列

​	队列（Queue）是一种先进先出（First In First Out, FIFO）的线性结构。队尾负责插入元素，队头负责删除元素。队列适合处理“先来的任务先处理”的场景，例如 BFS 层序遍历、任务调度、缓存窗口等。

### 常见队列结构

- 1.**普通队列**：只允许从队尾入队、从队头出队，常用于 BFS。
- 2.**双端队列 deque**：两端都可以插入和删除，常用于滑动窗口最大值、单调队列。
- 3.**优先队列 priority queue**：每次弹出优先级最高或最低的元素，通常用堆实现，常用于 Top K、合并有序数据、最短路径等问题。
- 4.**循环队列**：使用固定数组和两个指针模拟队列，可以节省移动元素的成本。

### 常用技巧

- 1.**BFS 层序遍历**。把起点放入队列，每次弹出当前节点，再把下一层节点放入队列。需要区分层数时，可以记录当前队列长度。
- 2.**去重访问**。图和矩阵 BFS 中，需要使用 visited 集合或直接修改原矩阵，避免重复入队。
- 3.**单调队列**。维护一个从队头到队尾单调递减或递增的 deque，保证队头始终是当前窗口答案。
- 4.**拓扑排序**。把入度为 0 的点放入队列，每弹出一个点就删除它的出边，并更新相邻节点入度。
- 5.**多源 BFS**。把多个起点同时入队，可以一次求所有点到最近起点的距离。

## 题型总结

### 基础题型

#### 232 Implement Queue using Stacks【Easy】

- 题意：使用两个栈实现队列的 push、pop、peek、empty 操作。
- 解题思路：`in_stack` 负责入队，`out_stack` 负责出队。当 `out_stack` 为空时，将 `in_stack` 中所有元素倒入 `out_stack`。
- code:

Python

```python
class MyQueue(object):

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.in_stack.append(x)

    def pop(self):
        """
        :rtype: int
        """
        self.peek()
        return self.out_stack.pop()

    def peek(self):
        """
        :rtype: int
        """
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.in_stack and not self.out_stack
```

### BFS

#### 200 Number of Islands【Medium】

- 题意：给定一个由 `1` 和 `0` 组成的二维网格，求岛屿数量。上下左右相邻的陆地属于同一个岛屿。
- 解题思路：遍历网格，遇到 `1` 时答案加一，并从这个点开始 BFS，把相连的陆地都标记成 `0`。
- code:

Python

```python
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != '1':
                    continue
                result += 1
                queue = [(i, j)]
                grid[i][j] = '0'
                for x, y in queue:
                    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == '1':
                            grid[nx][ny] = '0'
                            queue.append((nx, ny))
        return result
```

- 复杂度分析：时间复杂度 O(MN)，空间复杂度 O(MN)。

#### 207 Course Schedule【Medium】

- 题意：给定课程数量和先修关系，判断是否可以完成所有课程。
- 解题思路：使用拓扑排序。先统计每个节点的入度，把入度为 0 的课程加入队列。每学习一门课，就把它指向的后续课程入度减一。最后如果学习数量等于课程总数，则不存在环。
- code:

Python

```python
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
```

### 单调队列

#### 239 Sliding Window Maximum【Hard】

- 题意：给定数组和窗口大小 k，求每个窗口中的最大值。
- 解题思路：使用 deque 保存下标，并保证队列中的值单调递减。队头如果滑出窗口就弹出；新元素入队前，把队尾所有小于新元素的下标弹出。
- code:

Python

```python
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums or k <= 0:
            return []
        queue = []
        result = []
        for i, num in enumerate(nums):
            if queue and queue[0] <= i - k:
                queue.pop(0)
            while queue and nums[queue[-1]] <= num:
                queue.pop()
            queue.append(i)
            if i >= k - 1:
                result.append(nums[queue[0]])
        return result
```

### 优先队列

​	优先队列常用来处理“每次取最小/最大”的问题。Python 中可以使用 `heapq` 实现小根堆；如果需要大根堆，可以把数字取负后入堆。

> LeetCode 中含有队列的题目可以参考：[queue-leetcode-list.md](./queue-leetcode-list.md)

## 参考资料

- [Queue & Stack](https://leetcode.com/explore/learn/card/queue-stack/)
