1class Solution:
2    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
3        M = len(nums1)
4        N = len(nums2)
5        
6        result = []
7        
8        while M > 0 and N > 0:
9            if nums1[len(nums1) - M] < nums2[len(nums2) - N]:
10                result.append(nums1[len(nums1) - M])
11                M -= 1
12            else:
13                result.append(nums2[len(nums2) - N])
14                N -= 1
15            
16        if M:
17            for x in nums1[len(nums1) - M:]:
18                result.append(x)
19        
20        if N:
21            for x in nums2[len(nums2) - N:]:
22                result.append(x)
23        
24
25        # return result
26        
27        if len(result) % 2 == 0:
28            return (result[int(len(result) / 2 - 1)] + result[int(len(result) / 2)]) / 2
29        else:
30            return result[int((len(result)) // 2)]