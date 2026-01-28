1# https://leetcode.com/problems/merge-sorted-array/description/
2class Solution:
3    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
4        """
5        Do not return anything, modify nums1 in-place instead.
6        """
7        ptr_1 = 0
8        ptr_2 = 0
9        
10        while m and n:
11            if nums1[ptr_1] > nums2[ptr_2]:
12                nums1.insert(ptr_1, nums2[ptr_2])
13                nums1.pop()
14                ptr_1 += 1 # plus 1 due to an element inserted 
15                ptr_2 += 1
16                n -= 1
17            else:
18                ptr_1 += 1
19                m -= 1
20        
21        if n:
22            for i in nums2[ptr_2:]:
23                nums1.insert(ptr_1, i)
24                nums1.pop()
25                ptr_1 += 1