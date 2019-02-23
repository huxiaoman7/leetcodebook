## 数组

###  什么是数组

​	我们知道常用的数据存储方式有两种：顺序存储和非顺序存储。顺序存储就是把数据存储在一块连续的空间内。数组（array）就是典型的顺序存储，而链表就是典型的非顺序存储。

​	数组通常用于存储一系列相同类型的数据。当我们在创建数组时，会在内存中划分出一块连续的内存用于存储数据，插入数据时，会将数据按顺序存储在这块连续的内存中，读取时通过访问数组的索引迅速取出。数组名就是一个指针，指向这段内存的起始地址。通过数组的类型，编译器知道在访问下一个元素的时候需要在内存中后移多少个字节。由于数组在存储时是顺序存储的，存储数据的内存也是连续的，所以数组在读取数据时比较容易，随机访问速度快，但是插入和删除就比较费劲了。读取可以直接根据索引，插入和删除则比较耗时，插一个数据需要移动大量元素，在内存中空出一个元素的空间，然后将要增加的元素放在其中，如果想删除一个元素，同样需要移动大量元素去掉被移动的元素。所以如果需求是快速访问数据，很少或者几乎不插入和删除元素，数组是一个不错的选择。

​	最常见的有一维数组和二维数组，稍微复杂一点的是多维数组和动态数组。在c++中，STL提供了Vector，在Java中，Collection集合中提供了ArrayList和Vector,对于Python而言，内置的List就是一个动态指针数组。当列表中没有空间存储新的元素时，列表会动态地改变大小以容纳新的元素，每次改变大小时，会预留一部分空间以降低改变大小的频率。

### 类别
- 1.无序数组
    - 概念：未经过排序的数组
    - 优点：插入快
    - 缺点：查找慢，删除慢，大小固定
- 2.有序数组
    - 概念：数组中的元素是按照一定规则排列的。
    - 优点：查找效率高。根据元素值查找时可以使用二分查找，效率比无序数组高很多，在数据量大的时候尤其明显。对于leetcode中很多查找元素类的题目，如果没有事先说明是有序数组，可以事先对数组进行排序，再进行查找，二分法或其他方法都可以。
    - 缺点：插入和删除较慢。插入元素时，首先判断该元素的小标，然后对该小标之后的所有元素后移以为才能进行插入，所以有序数组比较适合查找频繁，而插入删除操作较少的情况。

        |   复杂度 | 有序数组 | 无序数组 |
        | :------| :------ | :------ |
        | 查找复杂度 | O(logn) | O(n) |
        | 插入复杂度 |O(n)| O(1) |

- 3.如何权衡
	- 根据需求性能判断：对于插入时性能要求高而对查询的要求不高或者插入操作远多于查询操作时，选择无序数组；相反，如果对查询性能要求较高或者查询操作量大时，则选择有序数组。
	- 根据数据量判断：数据量小且可预知，查询速度比插入速度更重要使用有序数组;数据量大且不可知，插入速度比查询速度更重要使用无序数组。

------

### 题型总结
【一维数组】
#### 1.K-Sum
​	这类题目通常会给定一个数组和一个值，让求出这个数组中两个/三个/K个值的和等于这个给定的值target。leetcode第一题就是two-sum，对于这类题目，首先看题目要求的时间复杂度和空间复杂度是什么，其次看有没有限制条件，如要求不能有重复的子数组或者要求按照升序/降序排列等。解法如下：
- 暴力解法：最常见，但是通常会超时，只能作为备选，
- hash-map：建立一个hash-map循环遍历一次即可
- two-pointers：定位两个指针根绝和的大小来移动另外一个。这里设定的指针个数根据题目中K的个数来定。3Sum中可以设定3个指针，固定两个，移动另一个


#### 2.区间问题
​	这类题目通常会给一个包含多个子数组的数组，然后针对区间是否重合来判断true or false。解题技巧：

> 1. 按start排序
> 2. 在前一个区间的end和后一个区间的start找交集

- 例题: [252 meeting room](https://leetcode.com/problems/meeting-rooms/)
- 题目理解：给定一个数组，包含每个会议的开始时间和结束时间[[s1,e1],[s2,e2],...] (si < ei),判断一个人能否参加所有的会议
- test case:
>Example1:
>Input: [[0,30],[5,10],[15,20]]
>Output: false
>Example2:
>Input: [[7,10],[2,4]]
>Output: true

- 解题思路：在这个题目里，如果一个人要参加所有会议，那么所有会议的时间应该不能重合，所以只需要判断后一个会议开始的start > 前一个会议结束的end就就可以，如果end>start,就返回false。首先得先对所有子数组的start进行排序，然后再进行判断start和end

Java解法
```
class Solution{
    public boolean canAttendMeetings(Interval[] intervals){
        Arrays.sort(intervals,(x,y)->(x.start-y.start);
        //i从1开始，因为涉及到判断前一个数组的end
        for (int i =0;i <intervals.length;i++){
            if (intervals[i-1].end > intervals[i].start){
                return false;
            }
}
return true;
```
Python解法
```
class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        intervals.sort(key=lambda x: x.start)
        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i-1].end:
                return False
        return True

```

#### 3.子数组类题目
&emsp;&emsp;这类题目通常会在一个包含多个子数组的数组中，求和/积，最大最小等。形式有很多种，例如求一个数组中和最小的子数组（209题），或者积最小的子数组（238题）
- 解题技巧：
    - 滑动窗口（sliding window）
- 例题：209 Minimum Size Subarray Sum[Medium]
- 题目理解：给定我们一个数字，让我们求子数组之和大于等于给定值的最小长度
- test case:
>Input: s = 7, nums = [2,3,1,2,4,3]
>Output: 2
>解释：满足子数组和=7的最小长度数组是[4,3],所以output=2
- 解题思路：求的数字要大于等于这个数字target，譬如这个testcase中，[2,3,1,2,4,3]，从前往后相加，前四项相加的和为8.已经大于7了，但是我们的target是7，后面的几项也都是正整数，继续往后走，肯定也会大于target7，所以这个时候我们把left指针往右移动一位，那么就是相当于成为了一个滑动窗口（sliding window），这种方法在String类型的题目出现的更多。
￼
- code:
Java解法
```java
class Solution {
    public int minSubArrayLen(int s, int[] nums) {
        int res = Integer.MAX_VALUE;//因为是求min，所以设定是Max_VALUE，然后最后的res比较就行，注意res不是0
        int left = 0,sum = 0;
        for (int i = 0;i<nums.length;i++){
            sum += nums[i];//每遍历一次，就把前i次数字相加求和
            while (left <=  i && sum >=s){
                res = Math.min(res, i-left+1);
                sum -= nums[left++];
            }
        }
        return res == Integer.MAX_VALUE? 0:res;
```
Python解法
```python
class Solution:

def minSubArrayLen(self, s, nums):
    total = left = 0
    result = len(nums) + 1
    for right, n in enumerate(nums):
        total += n
        while total >= s:
            result = min(result, right - left + 1)
            total -= nums[left]
            left += 1
    return result if result <= len(nums) else 0
```



### 二维数组

#### Rotate题型












