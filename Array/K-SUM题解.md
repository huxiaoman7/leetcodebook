### K-SUM总结&题解
### 题型总结


### 题目详解
# K-SUM

## 1.Two Sum

- 题目：1 Two sum  【easy】

- 解法：hash-map

- code

  Python

  ```python
  #hash-map
  class Solution(object):
      def twoSum(self, nums, target):
          """
          :type nums: List[int]
          :type target: int
          :rtype: List[int]
          """
          if len(nums) <= 1:
              return False
          keys = {}
          for i, v in enumerate(nums):
              if target-v in keys:
                  return [keys[target-v],i]
              else:
                  keys[v] = i
          return []
      
  ```

  





## 2.Two Sum II - Input array is sorted

-  题目：167 Two Sum II - Input array is sorted 【easy】

- 解法：

  - hash-map:排序了而已，和第一题很像啊，就是把下标改一下
  - 双指针：与二分法结合
  - 二分查找：

- code：

  Java

  ```java
  /*hash-map*/
  class Solution {
      public int[] twoSum(int[] numbers, int target) {
          int[] result = new int[2];
          HashMap<Integer,Integer> map = new HashMap<Integer,Integer>();
          for (int i = 0;i<numbers.length;i++){
          if (map.containsKey(target-numbers[i])){
              result[0]=map.get(target-numbers[i]);
              result[1]= i+1;
          }
          map.put(numbers[i],i+1);       
      }
          return result;
      }
  }
  ```

  

  Python

  ```python
  # 双指针法
  def twoSum1(self, numbers, target):
      l, r = 0, len(numbers)-1
      while l < r:
          s = numbers[l] + numbers[r]
          if s == target:
              return [l+1, r+1]
          elif s < target:
              l += 1
          else:
              r -= 1
   
  # dictionary           
  def twoSum2(self, numbers, target):
      dic = {}
      for i, num in enumerate(numbers):
          if target-num in dic:
              return [dic[target-num]+1, i+1]
          dic[num] = i
   
  # binary search        
  def twoSum(self, numbers, target):
      for i in xrange(len(numbers)):
          l, r = i+1, len(numbers)-1
          tmp = target - numbers[i]
          while l <= r:
              mid = l + (r-l)//2
              if numbers[mid] == tmp:
                  return [i+1, mid+1]
              elif numbers[mid] < tmp:
                  l = mid+1
              else:
                  r = mid-1
  ```

  
