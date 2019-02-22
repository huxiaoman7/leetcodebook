### 翻转类题型

最基础最常在面试中遇到的提醒，206一定要熟练掌握

- 例题：206 Reverse Linked List 【easy】

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
    - 时间复杂度：
    - 空间复杂度：
