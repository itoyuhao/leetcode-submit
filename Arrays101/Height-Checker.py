1# https://leetcode.com/problems/height-checker/description/
2class Solution:
3    def heightChecker(self, heights: List[int]) -> int:
4        origin = heights.copy()
5        n = len(heights)
6        # bubble sort
7        for i in range(n-1):
8            for j in range(n-i-1):
9                if heights[j] > heights[j+1]:
10                    heights[j], heights[j+1] = heights[j+1], heights[j]
11        
12        mismatch = 0
13        for i in range(n):
14            if origin[i] != heights[i]:
15                mismatch += 1
16        
17        return mismatch