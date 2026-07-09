# 栈知识点&题型总结

## 知识点

### 什么是栈

​	栈（Stack）是一种后进先出（Last In First Out, LIFO）的线性结构。只能在同一端进行插入和删除操作，这一端通常叫做栈顶。插入元素叫做入栈（push），删除元素叫做出栈（pop），读取栈顶元素叫做 peek/top。

​	栈适合处理“最近的状态优先被使用”的问题。例如括号匹配中，最后出现的左括号必须最先被匹配；表达式计算中，最近读到的操作数和操作符需要先参与计算；单调栈中，栈顶元素代表当前还没有找到答案的最近元素。

### 常用操作

| 操作 | 含义 | 时间复杂度 |
| ---- | ---- | ---------- |
| push | 元素入栈 | O(1) |
| pop | 栈顶元素出栈 | O(1) |
| top/peek | 获取栈顶元素 | O(1) |
| empty | 判断栈是否为空 | O(1) |

### 常用技巧

- 1.**括号匹配**。遇到左括号入栈，遇到右括号时检查栈顶是否匹配。如果最后栈为空，说明所有括号都被正确匹配。
- 2.**辅助栈**。当一个栈无法同时保存原始数据和附加信息时，可以再维护一个栈，例如 Min Stack 中用一个栈保存当前最小值。
- 3.**单调栈**。维护一个单调递增或单调递减的栈，用来寻找下一个更大/更小元素、柱状图面积、接雨水等问题。
- 4.**栈模拟递归**。二叉树前序、中序、后序遍历都可以用栈把系统递归显式写出来。
- 5.**表达式计算**。数字栈和符号栈配合，或者直接用一个栈保存中间结果，可以处理逆波兰表达式、基本计算器等问题。

## 题型总结

### 基础题型

#### 20 Valid Parentheses【Easy】

- 题意：给定只包含 `()[]{}` 的字符串，判断括号是否有效。
- test case:

> Input: "()[]{}"
>
> Output: true

- 解题思路：使用栈保存左括号。遇到右括号时，判断栈是否为空以及栈顶是否是对应的左括号；全部遍历后栈为空则合法。
- code:

Python

```python
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}
        for ch in s:
            if ch in mapping.values():
                stack.append(ch)
            else:
                if not stack or stack[-1] != mapping[ch]:
                    return False
                stack.pop()
        return not stack
```

- 复杂度分析：时间复杂度 O(N)，空间复杂度 O(N)。

#### 155 Min Stack【Easy】

- 题意：设计一个支持 push、pop、top，并且能在 O(1) 时间内返回最小值的栈。
- 解题思路：维护两个栈。一个栈保存所有元素，另一个栈保存每一步对应的当前最小值。入栈时，把 `min(x, min_stack[-1])` 放入辅助栈；出栈时两个栈同时弹出。
- code:

Python

```python
class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if self.min_stack:
            self.min_stack.append(min(x, self.min_stack[-1]))
        else:
            self.min_stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]
```

### 表达式计算

#### 150 Evaluate Reverse Polish Notation【Medium】

- 题意：给定逆波兰表达式，计算表达式的值。
- test case:

> Input: ["2", "1", "+", "3", "*"]
>
> Output: 9

- 解题思路：遇到数字入栈；遇到操作符时弹出两个数字进行计算，再把结果入栈。注意除法需要向 0 截断。
- code:

Python

```python
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for token in tokens:
            if token not in ['+', '-', '*', '/']:
                stack.append(int(token))
                continue
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            else:
                stack.append(int(float(a) / b))
        return stack[-1]
```

### 迭代极值

#### 84 Largest Rectangle in Histogram【Hard】

- 题意：给定柱状图每个柱子的高度，求能够组成的最大矩形面积。
- 解题思路：维护一个单调递增栈，栈中保存下标。当遇到更矮的柱子时，说明栈顶柱子的右边界已经确定，可以弹出计算面积。为了统一处理最后剩下的元素，可以在数组末尾补一个高度为 0 的柱子。
- code:

Python

```python
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        result = 0
        heights.append(0)
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                left = stack[-1] if stack else -1
                result = max(result, height * (i - left - 1))
            stack.append(i)
        heights.pop()
        return result
```

- 复杂度分析：每个元素最多入栈、出栈一次，时间复杂度 O(N)，空间复杂度 O(N)。

### 栈的应用

#### 栈模拟队列

​	232 Implement Queue using Stacks 使用两个栈实现队列。一个栈负责输入，一个栈负责输出。当输出栈为空时，把输入栈中的元素全部倒入输出栈，此时顺序就从后进先出变成了先进先出。

#### 栈模拟遍历

​	二叉树的前序、中序和后序遍历可以用栈实现。递归本质上使用的是系统调用栈，手写栈可以让遍历过程更可控，也能避免递归深度过大时栈溢出。

#### 单调栈

​	单调栈经常用于“找左边/右边第一个比当前元素大或小”的问题。常见题目有 84 Largest Rectangle in Histogram、85 Maximal Rectangle、316 Remove Duplicate Letters、402 Remove K Digits。

> LeetCode 中含有栈的题目可以参考：[stack-leetcode-list.md](./stack-leetcode-list.md)
