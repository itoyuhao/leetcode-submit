1# https://leetcode.com/problems/duplicate-zeros/description/
2class Solution:
3    def duplicateZeros(self, arr: List[int]) -> None:
4        """
5        Do not return anything, modify arr in-place instead.
6        """
7        # while-loop
8        n = len(arr)
9        next_ptr = 0
10        while next_ptr < n:
11            if arr[next_ptr] == 0:
12                arr.insert(next_ptr, 0)
13                arr.pop()
14                next_ptr += 1
15            next_ptr += 1
16        
17        # # for-loop
18        # n = len(arr)
19        # zero_cnt = 0
20        # for i in range(n):
21        #     if i + zero_cnt >= n:
22        #         break
23        #     if arr[i+zero_cnt]  == 0:
24        #         arr.insert(i+zero_cnt, 0)
25        #         arr.pop()
26        #         zero_cnt += 1
27        
28        
29                