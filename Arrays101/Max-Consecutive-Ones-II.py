1# https://leetcode.com/problems/max-consecutive-ones-ii/description/
2class Solution:
3    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
4        max_record = 0
5        left, right = 0, 0
6        num_zeroes = 0
7
8        while right < len(nums):
9            if nums[right] == 0:
10                num_zeroes += 1
11            while num_zeroes == 2:
12                if nums[left] == 0:
13                    num_zeroes -= 1
14                left += 1
15            
16            max_record = max(max_record, right - left + 1)
17
18            right += 1
19
20        return max_record
21
22        # n = len(nums)
23        
24        # life = 1
25        # consecutive = 0
26        # for i in range(n):
27        #     if nums[i] == 1:
28        #         consecutive += 1
29        #     else:  # nums[i] == 0
30        #         if life:
31        #             life = 0
32        #             consecutive += 1
33        #             what_if = 1
34        #         else:
35        #             life = 1
36        #             if consecutive > max_record:
37        #                 max_record = consecutive
38        #             consecutive = 0
39                    
40        
41        # if consecutive > max_record:
42        #     max_record = consecutive
43            
44        # return max_record
45                        
46                        