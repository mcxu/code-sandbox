'''
Floyds cycle detection algorithm for array duplicates

Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), 
prove that at least one duplicate number must exist. Assume that there is only one duplicate number, 
find the duplicate one.

Example 1:
Input: [1,3,4,2,2]
Output: 2

Example 2:
Input: [3,1,3,4,2]
Output: 3
Note:

You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.

https://leetcode.com/problems/find-the-duplicate-number/
https://kennyzhuang.gitbooks.io/algorithms-collection/content/find_the_duplicate_number.html
'''

class Solution:
    def findDuplicate(self, nums) -> int:
        # create a graph
        slow = nums[0] # index (0) points to value at that index
        fast = nums[nums[0]] # (index (0) -> value at that index) becomes index -> value at that index
        print("A slow: {}, fast: {}".format(slow, fast))
        while slow != fast:
            slow = nums[slow] 
            fast = nums[nums[fast]]
            print("B slow: {}, fast: {}".format(slow, fast))
            
        print("a cycle was found because: slow={}, fast={}".format(slow,fast))    
        # At this point the 1st while loop has found that there IS a cycle (there exists a duplicate)
        # But just because slow == fast, it doesn't meant that this value is where the cycle BEGINS! 
        # To find the duplicate val where the cycle actual begins, have 2 pointers, one at index 0 of nums 
        # and 1 at the last value of slow from previous loop. Then increment each until equal. 
        # (See linked list implementation: code-sandbox\PythonSandbox\src\misc\floyd_cycle_detection_linked_list.py) 
        temp = 0 # index 0 of nums
        while temp != slow:
            temp = nums[temp]
            slow = nums[slow]
            print("C temp: {}, slow: {}".format(temp, slow))
            
        return slow
            
    def test1(self):
        # slow graph: 0 -> 1 -> 3 -> (2) -> 4 -> 2 -> 4 -> ...
        # fast graph: 0 -> 1 -> 2 -> (2) -> 2 -> 2 -> 2 -> ...
        # cycle begins at (2)'s in each slow and fast graphs.
        nums = [1,3,4,2,2]
        ans = self.findDuplicate(nums)
        print("test1: ans: ", ans)
    
    def test2(self):
        nums = [2,3,4,2,2]
        ans = self.findDuplicate(nums)
        print("test2: ans: ", ans)
    
    def test3(self):
        nums = [2,5,9,6,9,3,8,9,7,1]
        ans = self.findDuplicate(nums)
        print("test3: ans: ", ans)

sol = Solution()
#sol.test1()
#sol.test2()
sol.test3()
