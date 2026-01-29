1# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
2class Solution:
3    def twoSum(self, numbers: List[int], target: int) -> List[int]:
4        # how to use binary search?
5        
6        if len(numbers) == 2:
7            return [1, 2]
8        
9        low, high = 0, len(numbers) - 1
10        
11        while low < high:
12            
13            sum = numbers[low] + numbers[high]
14            
15            if sum == target:
16                return [low + 1, high + 1]
17            
18            elif sum > target:
19                high -= 1
20            
21            else:
22                low += 1
23        
24        return [low + 1, high + 1]