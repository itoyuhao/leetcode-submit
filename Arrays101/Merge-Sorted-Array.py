# https://leetcode.com/problems/merge-sorted-array/description/
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ptr_1 = 0
        ptr_2 = 0
        
        while m and n:
            if nums1[ptr_1] > nums2[ptr_2]:
                nums1.insert(ptr_1, nums2[ptr_2])
                nums1.pop()
                ptr_1 += 1 # plus 1 due to an element inserted 
                ptr_2 += 1
                n -= 1
            else:
                ptr_1 += 1
                m -= 1
        
        if n:
            for i in nums2[ptr_2:]:
                nums1.insert(ptr_1, i)
                nums1.pop()
                ptr_1 += 1