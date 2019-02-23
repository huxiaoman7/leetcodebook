## LeetCode链表知识点&题型总结

## 知识点


### 什么是链表

​	链表(Linked List)是一种常见的线性结构。它不需要一块连续的内存空间，通过指针即可将一组零散的内存块串联起来。我们把内存块成为链表的节点，为了将所有的节点串起来，每个链表的节点除了存储数据之外，还需要记录链表的下一个节点的地址，这个记录下个节点地址的指针我们叫做**后驱指针**。搜索链表需要O(N)的时间复杂度，这点和数组类似，但是链表不能像数组一样，通过索引的方式以O(1)的时间读取第n个数。链表的优势在于能够以较高的效率在任意位置插入或者删除一个节点。

### 类别

#### 单向链表

​	每个节点有一个next指针指向后一个节点，还有一个成员变量用于存储数值。单向链表中有两个节点比较特殊，分别是头结点和尾节点。头结点用来记录链表的基地址，知道头结点我们就可以遍历得到整条链表。尾结点的特殊在于指针指向的是一个空指针NULL。

![image](https://raw.githubusercontent.com/huxiaoman7/leetcodebook/master/Linklist/pic/1.png)



#### 循环链表

​	循环链表是一种特殊的单链表，与单链表不同的是尾节点不指向空地址，指向链表的头结点。优点是从链尾到链头比较方便，当要处理的数据具有环形结构特点是，非常适合用循环链表来处理。

![image](https://raw.githubusercontent.com/huxiaoman7/leetcodebook/master/Linklist/pic/2.png)


#### 双向链表

​	双向链表支持两个方向，每个节点不只有一个后驱指针next指向后面的节点，还有一个前驱指针prev指向前面的节点。

![image](https://raw.githubusercontent.com/huxiaoman7/leetcodebook/master/Linklist/pic/3.png)

#### 双向循环链表

![image](https://raw.githubusercontent.com/huxiaoman7/leetcodebook/master/Linklist/pic/4.png)

### 与数组的性能对比

| 时间复杂度 | 数组    | 链表   |
| ---- | ------------------------------------------------------------ | ------ |
| 插入删除   |O(n)| O(1) |
| 随机访问   |O(1)| O(n)|





### 优缺点

- 优点：动态扩容，不需要占用过多的内存
- 缺点：不能随机访问，如果要访问一个元素的话，不能根据索引访问，只能从头开始遍历，找到对应的元素

### 常用技巧

- 1.**使用dummy node**。dummy node就是在链表的head前加一个节点指向head，即dummy->head，可以理解成一个虚拟节点。多针对于单链表没有前向指针的问题，保证链表的head不会在删除操作中丢失。通常情况下，如果链表的head会发生变化，譬如删除或者被修改等，可以创建dummy node：

  ```java
  ListNode dummy = new ListNode(0);
  dummy.next = head;
  ```

  这样就使得操作head节点与操作其他节点没有区别。

- 2.**双指针法**。对于寻找链表的某个特定位置，或者判断是否有环等问题时，可以用两个指针变量fast和slow:

  ```java
  ListNode slow = head;
  ListNode fast = head;
  ```

  以不同的速度遍历该链表，以找到目标位置。注意：在测试时，需要分别选取链表长度为奇数和偶数的test case，可以验证算法在一般情况下的正确性避免遗漏。

- 3.**交换节点的处理**。如果需要交换两个节点的位置，譬如24题 [Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/),需要交换两个相邻位置的节点，对于这两个前驱节点，他们的next指针会受到影响，这两个节点本身也会受到影响，可以用一下步骤：

  - 1）先交换两个前驱节点的next指针的值
  - 2）再交换这两个节点的next指针的值

  无论这两个节点的相对位置和绝对位置如何，以上的处理方式均可成立

- 4.**同时操作两个链表的处理**。遇到这种题目，循环的条件一般可以用while（list1 && list2），当循环跳出来后，再处理剩下非空的链表，这相当于：边界情况特殊处理，常规情况常规处理。



## 题型总结

### 基本操作

#### 删除类

- 例题：19 Remove Nth Node From End of List 【Medium】
- 题意：删除链表中倒数第n个节点
- test case:

> Given linked list: 1->2->3->4->5, and n = 2.
>
> 删除链表中导数第二个节点，变成1->2->3->5.

- 解题思路：*双指针法* 。在head前加一个虚拟节点dummy node，并设置两个指针fast和slow。 fast指针现象前移动n个节点（从dummy节点开始移动，所以实际上是移动到了n-1位），然后fast和slow同时开始移动，当fast.next == None时，slow节点指向的就是需要删除的节点前面的一个节点，将其指向.next.next即可
- code：

Java

```java
class Solution{
public static ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode fast = dummy;
        ListNode slow = dummy;
        while(fast.next != null){
        	if(n <= 0)
        		slow = slow.next;
        	fast = fast.next;
        	n--;
        }
        if(slow.next != null)
        	slow.next = slow.next.next;
        return dummy.next;
    }
}
```



Python

```python
class Solution:
    def removeNthFromEnd(self, head, n):
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head
```



- 复杂度分析：时间复杂度O(length(list)), 即O(N)，空间复杂度O(1)

> Leetcode中包含删除类的题目：

| 序号 | 题目                                                         | 难度   | 代码              |
| ---- | ------------------------------------------------------------ | ------ | ----------------- |
| 19   | [Remove   Nth Node From End of List    ](https://leetcode.com/problems/remove-nth-node-from-end-of-list) | medium | python、java、c++ |
| 82   | [Remove   Duplicates from Sorted List II    ](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii) | Medium | python、java、c++ |
| 83   | [Remove   Duplicates from Sorted List    ](https://leetcode.com/problems/remove-duplicates-from-sorted-list) | Easy   | python、java、c++ |
| 203  | [Remove   Linked List Elements    ](https://leetcode.com/problems/remove-linked-list-elements) | Easy   | python、java、c++ |
| 237  | [Delete Node   in a Linked List    ](https://leetcode.com/problems/delete-node-in-a-linked-list) | Easy   | python、java、c++ |



### 翻转类题型

最基础最常在面试中遇到的提醒，206一定要熟练掌握

- 例题1：206 Reverse Linked List 【easy】

- 题意：翻转一个单向链表

- test case:

  > Input：1->2->3->4->5->NULL
  >
  > Output：5->4->3->2->1->NULL

- 思考：可否用迭代和递归两种方法完成？

- 解题思路：对于翻转类的题型，我们只需要知道head->prev节点如何翻转成prev-head即可,这里我们仍然要用到dummy node，作为head的前驱节点，在翻转前，是dummy->head->2->3…->NULL,翻转后变成NULL->5->…->2->head->dummy，dummy变成了尾节点，因为这是一个单向链表，head只有一个指针，已经指向了下一个节点了，所以首先需要把head的下一个节点，即head.next用一个临时变量存储起来，与head'断开连接'，这样head就可以指向dummy了，即我们将dummy->head变成了head->dummy，第一步完成。后面的处理方式有两种写法，一种是迭代，我们可以再来用同样的方式处理head->head.next ,使之变成head.next->head，同样让head.next.next用一个变量存储起来断开与head.next的连接，然后head.next指向head即可，在这里其实head.next.next就相当于第一步中的head.next,head.next就相当于第一步的dummy,所以可以直接写成dummy = head，head = next；递归的方式则需要c创建一个递归函数，把第一步的步骤写入递归函数里面，然后再不断地调用这个递归函数即可。

- code：

  Java

  ```java
  /*迭代写法*/
  class Solution {
      public ListNode reverseList(ListNode head) {
          if (head == null || head.next == null){
              return head;
          }
          ListNode dummy = null;
          while (head != null){
              ListNode next = head.next;
              head.next = dummy;
              dummy = head;
              head = next;
          } 
          return dummy;
      }
  }
  
  
  /*递归写法*/
  class Solution{
      public ListNode reverseList(ListNode head) {
          return reverseListHelper(head, null);
      }
  
      private ListNode reverseListHelper(ListNode head, ListNode newHead) {
          if (head == null)
              return newHead;
          ListNode next = head.next;
          head.next = newHead;
          return reverseListHelper(next, head);
      }
  }
  
  ```

  

  

  Python

  ```python
  # 迭代写法
  class Solution(object):
      def reverseList(self, head):
          """
          :type head: ListNode
          :rtype: ListNode
          """
          dummy = None
          while head :
              next = head.next
              head.next = dummy
              dummy = head
              head = next
          return dummy
      
  # 递归写法
  class Solution(object):
      def reverseList(self,head):
          """
          :type head: ListNode
          :rtype: ListNode
          """
          return self.reverseListHelper(head)
      
      def reverseListHelper(self,head,dummy=None):
          if not head:
              return dummy
          next = head.next
          head.next = dummy
          return self.reverseListHelper(next,head)
  ```

  - 复杂度分析：

    | 复杂度     | 迭代法 | 递归法 |
    | ---------- | ------ | ------ |
    | 时间复杂度 | O(N)   | O(N)   |
    | 空间复杂度 | O(1)   | O(N)   |

    

    

- 例题2：92 Reverse Linked List 【medium】

- 题意：从m->n的位置翻转链表($1 \leq m \leq n \leq length(list)$ )

- test case:

  > Input:1->2->3->4->5->NULL, m = 2, n = 4
  >
  > Output:1->4->3->2->5->NULL

  

- 解题思路：迭代法。翻转链表第一步找起始位置和它前面的节点，头结点的前驱节点我们还是设置dummy，从m->n翻转，那么在开始处设置为start node，后驱节点设置为then, 即start.next = then，来帮助我们翻转。以test case 为例，下面是第一次翻转：

![image](https://raw.githubusercontent.com/huxiaoman7/leetcodebook/master/Linklist/pic/5.png)
​	第一次翻转完成之后，如图所示 由 dummy->1 - 2 - 3 - 4 - 5  变成了 dummy->1 - 3 - 2 - 4 - 5，同理，迭代，第二次翻转后 由 dummy->1 - 3 - 2 - 4 - 5  变成 dummy->1 - 4 - 3 - 2 - 5，翻转结束。简单来说，相当于不断地交换then和start，然后将then后移直到结束。

- code：

  ```java
  /*迭代法*/
  class Solution{
      public ListNode reverseBetween(ListNode head, int m, int n) {
      if(head == null) return null;
      ListNode dummy = new ListNode(0); // 创建一个 dummy node 标记这个链表的head
     
      dummy.next = head;
      ListNode pre = dummy; 
          
      // dummy-> 1 -> 2 -> 3 -> 4 -> 5
          
      for(int i = 0; i< m-1; i++) pre = pre.next;
      
      ListNode start =pre.next; 
      ListNode then = start.next; // 创建一个 then node 帮助后面翻转
      
      // 1 - 2 -3 - 4 - 5 ; m=2; n =4 ---> pre = 1, start = 2, then = 3
          
      for(int i=0; i<n-m; i++)
      {
          start.next = then.next; 
          then.next = pre.next;
          pre.next = then;
          then = start.next;
      }
      return dummy.next;    
  }
  
  /*递归法*/
  class Solution {
      private boolean stop;
      private ListNode left;
      public void recurseAndReverse(ListNode right, int m, int n) {
          if (n == 1) {
              return;
          }
          right = right.next;
  
          if (m > 1) {
              this.left = this.left.next;
          }
  
          this.recurseAndReverse(right, m - 1, n - 1);
  
          if (this.left == right || right.next == this.left) {
              this.stop = true;            
          }
  
          if (!this.stop) {
              int t = this.left.val;
              this.left.val = right.val;
              right.val = t;
              this.left = this.left.next;
          }
      }
  
      public ListNode reverseBetween(ListNode head, int m, int n) {
          this.left = head;
          this.stop = false;
          this.recurseAndReverse(head, m, n);
          return head;
      }
  }
  ```

  Python

  ```python
  # 迭代法
  class Solution(object):
      def reverseBetween(self, head, m, n):
          dummy = ListNode(0)
          dummy.next = head
          
          cur, prev = head, dummy
          for _ in xrange(m - 1):
              cur = cur.next
              prev = prev.next
          
          for _ in xrange(n - m):
              temp = cur.next
              cur.next = temp.next
              temp.next = prev.next
              prev.next = temp
  
          return dummy.next
      
  # 递归法
  class Solution:
      def reverseBetween(self, head, m, n):
          def reverse(prev, current, m):
              nxt = current.next
              current.next = prev
              if m == 0:
                  return current, nxt
              return reverse(current, nxt, m - 1)
  
          lth = None
          mth = head
  
          for i in range(1, m):
              lth = mth
              mth = mth.next
  
          nth, oth = reverse(lth, mth, n - m)
          if lth:
              lth.next = nth
          else:
              head = nth
          mth.next = oth
          return head
  ```

  

- 复杂度分析：

  

- | 复杂度     | 迭代法 | 递归法 |
  | ---------- | ------ | ------ |
  | 时间复杂度 | O(N)   | O(N)   |
  | 空间复杂度 | O(1)   | O(N)   |

  迭代法：时间复杂度是O(N), 并且我们是在原链表上进行指针移动的，所以空间复杂度为O(1)

  

  递归法：每个节点最多需遍历两次，一次是常规的递归，一次是回溯的递归，所以时间复杂度是O(N)，在最坏的情况下，我们需要翻转整个链表，并且递归的方法会占用栈，所以空间复杂度是O(N)

  

  这是两个非常典型而且常见的链表翻转类题目，在面试中也经常出现作为热身题，所以需要重点关注。

  > Leetcode中包含翻转链表的题目：	

| 序号 | 题目                                                         | 难度   | 代码              |
| ---- | ------------------------------------------------------------ | ------ | ----------------- |
| 25   | [Reverse Nodes   in k-Group    ](https://leetcode.com/problems/reverse-nodes-in-k-group) | Hard   | python、java、c++ |
| 61   | [Rotate   List    ](https://leetcode.com/problems/rotate-list) | Medium | python、java、c++ |
| 92   | [Reverse   Linked List II    ](https://leetcode.com/problems/reverse-linked-list-ii) | Medium | python、java、c++ |
| 206  | [Reverse   Linked List    ](https://leetcode.com/problems/reverse-linked-list) | Easy   | python、java、c++ |



### 合并链表

- 例题：21 Merge Two Sorted Lists 【easy】

- 题意：将两个排序好的链表合并成新的有序链表

- test case:

  > Input: 1->2->4, 1->3->4
  >
  > Output: 1->1->2->3->4->4


- 解题思路: **迭代法和递归法**。迭代法是每次比较两个结点，把较小的加到结果链表中，并且这个指针向后移动；递归法即每次比较两个链表的头部，将较小的头部单独取出来，剩下的两个部分继续递归。
- code：

Java

```java
/*迭代法*/
class Solution{
public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
		ListNode head = new ListNode(0);
		ListNode cur = head;
		while (l1 != null && l2 != null) {
			if (l1.val >= l2.val) {
				cur.next = l2;
				l2 = l2.next;
			} else {
				cur.next = l1;
				l1 = l1.next;
			}
			cur = cur.next;
		}
 
		if (l1 != null)
			cur.next = l1;
		if (l2 != null)
			cur.next = l2;
		return head.next;
	}
}

/*递归法*/
class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        if (l1 == null) return l2;
        if (l2 == null) return l1;
        if (l1.val > l2.val) {
            ListNode tmp = l2;
            tmp.next = mergeTwoLists(l1, l2.next);
            return tmp;
        } else {
            ListNode tmp = l1;
            tmp.next = mergeTwoLists(l1.next, l2);
            return tmp;
        }
    }
}
```



Python

```python
# 迭代法
def mergeTwoLists1(self, l1, l2):
    dummy = cur = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    cur.next = l1 or l2
    return dummy.next
    
# 递归法    
def mergeTwoLists2(self, l1, l2):
    if not l1 or not l2:
        return l1 or l2
    if l1.val < l2.val:
        l1.next = self.mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = self.mergeTwoLists(l1, l2.next)
        return l2
```



> LeetCode中包含 合并链表类的题目：

| 序号 | 题目                                                         | 难度   | 代码              |
| ---- | ------------------------------------------------------------ | ------ | ----------------- |
| 2    | [Add   Two Numbers    ](https://leetcode.com/problems/add-two-numbers) | medium | python、java、c++ |
| 21   | [Merge   Two Sorted Lists    ](https://leetcode.com/problems/merge-two-sorted-lists) | Easy   | python、java、c++ |
| 23   | [Merge   k Sorted Lists    ](https://leetcode.com/problems/merge-k-sorted-lists) | Hard   | python、java、c++ |
| 445  | [Add   Two Numbers II    ](https://leetcode.com/problems/add-two-numbers-ii) | Medium | python、java、c++ |



### 环形链表

- 例题：141 Linked List Cycle 【easy】

- 题意：判断一个单链表是否存在环

- test case:

  > Input : head = [3, 2, 0, -4], pos = 1
  >
  > Output : true
  >
  > why：在这个单链表中存在一个环，尾节点指向第二个节点  

  

- 解题思路：**双指针法**。这道题可以用双指针做，有的也叫快慢指针，或者runner and chaser，意思是从头设置两个指针，一个快指针走2n步（视具体题目而定），慢指针走n步，当快指针走到尾节点时，满指针正好走到链表的一半（视具体题目而定）。在本题中，设置快指针走两步，慢指针一次走一步，如果快指针走到了尽头，则说明链表无环，如果快指针和慢指针相遇就说明链表有环。为什么呢？我们假设一个有环链表，快慢指针最后都会走到环上，而这个环就像一个环形跑道一样，慢指针在后面，快指针在前面，但实际上快指针也在追慢指针，希望能超慢指针一圈。他们在这个跑道上，总会有一天快指针追上了慢指针。我们不用担心快指针跳过了慢指针，因为他们两的速度差是1，所以它们在环上的距离总是每次减1，最后总能减到0。

- code：

Java

```java
public class Solution {
    public boolean hasCycle(ListNode head) {
    if(head==null) return false;
    ListNode slow = head;
    ListNode fast = head;
    while(fast.next!=null && fast.next.next!=null) {
        slow = slow.next;
        fast = fast.next.next;
        if(slow==fast) return true;
    }
    return false;
    }
}
```



Python

```python
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
      
        try:
            slow = head
            fast = head.next
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False
```

- 复杂度分析：时间复杂度O(N)，空间复杂度 O(1)

> LeetCode中含有环形链表的题目：

| 序号 | 题目                                                         | 难度   | 代码              |
| ---- | ------------------------------------------------------------ | ------ | ----------------- |
| 141  | [Linked   List Cycle    ](https://leetcode.com/problems/linked-list-cycle) | Easy   | python、java、c++ |
| 142  | [Linked   List Cycle II    ](https://leetcode.com/problems/linked-list-cycle-ii) | Medium | python、java、c++ |
| 708  | [Insert   into a Cyclic Sorted List    ](https://leetcode.com/problems/insert-into-a-cyclic-sorted-list) | Medium | python、java、c++ |



### 拆分链表

- 例题：86 Partition List 【medium】

- 题意：给定一个链表以及一个目标值，把小于该目标值的所有节点都移至链表的前端，**大于或等于**目标值的节点移至链表的尾端，**同时要保持这两部分在原先链表中的相对位置。**

- test case:

- 解题思路: **二分法**。设置两个指针left和right，顺序遍历整条链表，left、mid、target三者比较，根据情况left右移或者right左移。关键就在于边界情况和元素有重复。

  - 当 nums[mid] = nums[left] 时，这时由于很难判断 target 会落在哪，那么只能采取 left++

  - 当 nums[mid] > nums[left] 时，这时可以分为两种情况，判断左半部比较简单

  - 当 nums[mid] < nums[left] 时，这时可以分为两种情况，判断右半部比较简单

    

- code：

Java

```java
class Solution {
    public boolean search(int[] nums, int target) {
        int left = 0, right = nums.length - 1;
        
        while (left <= right) {
            int mid = (left + right) / 2;
            if (target == nums[mid]) return true;
            if (nums[mid] == nums[left]) left++;
            
            else if (nums[mid] > nums[left]) {
                if (nums[left] <= target && nums[mid] > target) right = mid - 1;
                else left = mid + 1;
            } else {
                if (nums[mid] < target && target <= nums[right]) left = mid + 1;
                else right = mid - 1;
            }
        }
        return false;
    }
}
```



Python

```python
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] == target:
                return True
            while left < mid and nums[left] == nums[mid]: 
                left += 1
            
            if nums[left] <= nums[mid]:
                
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
               
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False
```



- 复杂度分析：

> LeetCode中含有拆分类的题目：

| 序号 | 题目                                                         | 难度   | 代码              |
| ---- | ------------------------------------------------------------ | ------ | ----------------- |
| 725  | [Split Linked   List in Parts    ](https://leetcode.com/problems/split-linked-list-in-parts) | Medium | python、java、c++ |
| ---- | ------------------------------------------------------------ | ------ | ----------------- |
| 86   | [Partition   List    ](https://leetcode.com/problems/partition-list) | Medium | python、java、c++ |



### 排序链表

- 例题：148 Sort List【medium】
- 题意：在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序
- test case:

>Input: 4->2->1->3
>
>Output: 1->2->3->4

- 解题思路 : **归并排序**。这题有很多解法，题目要有时间复杂度是O(nlogn),满足这个条件的有快速排序，堆排序，归并排序，三者的空间复杂度分别为O(1),O(N),)O(N)。对于链表而言，在进行归并操作时并不需要像数组的归并操作那样分配一个临时数组空间，所以是O(1)的空间复杂度，只需要改变节点的next指针的指向，就可以表示新的归并后的顺序。
- 思考：快排和归并排序的时间复杂度都是O(nlogn)，实践证明快排的速度比归并排序的速度更快，对于数组排序成立，为什么在链表中归并排序更快呢？
- code：

Java

```java
public class Solution {
  
  public ListNode sortList(ListNode head) {
    if (head == null || head.next == null)
      return head;
        
    // step 1.把链表分成两半
    ListNode prev = null, slow = head, fast = head;
    
    while (fast != null && fast.next != null) {
      prev = slow;
      slow = slow.next;
      fast = fast.next.next;
    }
    
    prev.next = null;
    
    // step 2.对于每一部分的链表进行排序
    ListNode l1 = sortList(head);
    ListNode l2 = sortList(slow);
    
    // step 3. 合并 l2 和 l2
    return merge(l1, l2);
  }
  
  ListNode merge(ListNode l1, ListNode l2) {
    ListNode l = new ListNode(0), p = l;
    
    while (l1 != null && l2 != null) {
      if (l1.val < l2.val) {
        p.next = l1;
        l1 = l1.next;
      } else {
        p.next = l2;
        l2 = l2.next;
      }
      p = p.next;
    }
    
    if (l1 != null)
      p.next = l1;
    
    if (l2 != null)
      p.next = l2;
    
    return l.next;
  }

}
```



Python

```python
class Solution(object):
    def sortList(self, head):
        if not head or not head.next:
            return head
        fast, slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        second = slow.next
        slow.next = None
        l = self.sortList(head)
        r = self.sortList(second)
        return self.merge(l, r)
    
    def merge(self, l, r):
        if not l or not r:
            return l or r
        if l.val > r.val:
            l, r = r, l
        head = pre = l
        l = l.next
        while l and r:
            if l.val < r.val:
                l = l.next
            else:
                nxt = pre.next
                pre.next = r
                tmp = r.next
                r.next = nxt
                r = tmp
            pre = pre.next
        pre.next = l or r
        return head
```



- 思考解答：如果待排序的元素存储在数组中，那么快速排序相对归并排序就有两个原因更快。一是，可以很快地进行元素的读取(相对于链表，数组的元素是顺序摆放的，而链表的元素是随机摆放的)，数组的partion这步就比链表的partion这步快。二是，归并排序在merge阶段需要辅助数组，需要申请O(N)的空间，申请空间也是需要时间的。而快排不需要额外申请空间。如果待排序的元素存储在链表中，快排的优点就变成了缺点。归并排序于是就速度更优了。

> LeetCode中 包含链表排序的题目：

| 序号 | 题目                                                         | 难度   | 代码              |
| ---- | ------------------------------------------------------------ | ------ | ----------------- |
| 143  | [Reorder List    ](https://leetcode.com/problems/reorder-list) | Medium | python、java、c++ |
| ---- | ------------------------------------------------------------ | ------ | ----------------- |
| 147  | [Insertion   Sort List    ](https://leetcode.com/problems/insertion-sort-list) | Medium | python、java、c++ |
| 148  | [Sort List    ](https://leetcode.com/problems/sort-list)     | Medium | python、java、c++ |

####  

参考资料：

1.http://stackoverflow.com/questions/7629904/why-is-mergesort-better-for-linked-lists

2.https://leetcode.com/problems/sort-list/discuss/46714/Java-merge-sort-solution

3.https://blog.csdn.net/happyaaaaaaaaaaa/article/details/51602234

4.https://leetcode.com/problems/merge-two-sorted-lists/discuss/9735/Python-solutions-(iteratively-recursively-iteratively-in-place).






