1# https://leetcode.com/problems/valid-mountain-array/description/
2class Solution:
3    def validMountainArray(self, arr: List[int]) -> bool:
4        n = len(arr)
5        
6        if n < 3:
7            return False
8        
9        increasing = True
10        for i in range(n-1):
11            if arr[i] == arr[i+1]:  # not strictly ordered
12                return False
13            if increasing and (arr[i+1] - arr[i] < 0):
14                top = i #  record index of mountain top
15                increasing = False
16            if not increasing and (arr[i+1] - arr[i] > 0):
17                return False
18        
19        
20        return True if not increasing and top != 0 else False
21                