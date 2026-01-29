1# https://leetcode.com/problems/find-the-duplicate-number/description/
2class Solution:
3    def findDuplicate(self, nums: List[int]) -> int:
4        # # approah 1: sort and iterate
5        # nums.sort()
6        
7        # seen = nums[0]
8        
9        # for i in range(1, len(nums)):
10        #     if nums[i] == seen:
11        #         return seen
12        #     else:
13        #         seen = nums[i]
14        
15        # approach 2: Negative Marking
16
17        # for num in nums:
18        #     cur = abs(num)
19        #     if nums[cur] < 0:
20        #         duplicate = cur
21        #         break
22        #     nums[cur] = -nums[cur]
23        
24        # for i in range(len(nums)):
25        #     nums[i] = abs(nums[i])
26        
27        # return duplicate
28
29        # approach 3: binary search
30        low = 1
31        high = len(nums) - 1
32        
33        while low <= high:
34            cur = (low + high) // 2
35            count = 0
36
37            count = sum(num <= cur for num in nums)
38            if count > cur:
39                duplicate = cur
40                high = cur - 1
41            else:
42                low = cur + 1
43        
44        return duplicate