1# https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/description/
2# """
3# This is ArrayReader's API interface.
4# You should not implement it, or speculate about its implementation
5# """
6#class ArrayReader:
7#    def get(self, index: int) -> int:
8
9class Solution:
10    def search(self, reader: 'ArrayReader', target: int) -> int:
11        
12        # idea: create a while-loop to do doubling whenever the upper bound is smaller than the target
13                # end looping when we find an index that is greater than target value
14                # then we do binary search
15        
16        
17        left, right = 0, 1
18        
19        if reader.get(left) == target:
20            return 0
21        
22        # finding lower/upper bound
23        while reader.get(right) < target:
24            left = right
25            right = right * 2
26        
27        # doing binary search
28        while left <= right:
29            mid = (left + right) // 2
30            if reader.get(mid) == target:
31                return mid
32            elif reader.get(mid) > target:
33                right = mid - 1
34            
35            else:
36                left = mid + 1
37        
38        return -1
39            