1# https://leetcode.com/problems/squares-of-a-sorted-array/description/
2class Solution:
3    def sortedSquares(self, nums: List[int]) -> List[int]:
4        res = []
5        
6        start_pointer = 0
7        end_pointer = len(nums) - 1
8        
9        
10        while start_pointer < end_pointer:
11            if nums[start_pointer] * nums[start_pointer] >= nums[end_pointer] * nums[end_pointer]:
12                res.insert(0, nums[start_pointer]*nums[start_pointer])
13                start_pointer += 1
14            else:
15                res.insert(0, nums[end_pointer]*nums[end_pointer])
16                end_pointer -= 1
17        
18        res.insert(0, nums[start_pointer]*nums[start_pointer])
19        
20        return res