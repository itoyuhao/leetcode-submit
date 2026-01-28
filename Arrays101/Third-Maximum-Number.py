1class Solution:
2    def thirdMax(self, nums: List[int]) -> int:
3        # sort 
4        n = len(nums)
5        
6        if n < 3:
7            return max(nums)
8        
9        for i in range(n-1):
10            max_idx = i
11            for j in range(i, n):
12                if nums[max_idx] < nums[j]:
13                    max_idx = j
14            nums[max_idx], nums[i] = nums[i], nums[max_idx]
15        
16        rank = 1
17        for i in range(n-1):
18            if nums[i] > nums[i+1]:
19                rank += 1
20            if rank == 3:
21                return nums[i+1]
22        
23        return nums[0]