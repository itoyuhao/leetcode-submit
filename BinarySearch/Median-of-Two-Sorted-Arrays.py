class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        M = len(nums1)
        N = len(nums2)
        
        result = []
        
        while M > 0 and N > 0:
            if nums1[len(nums1) - M] < nums2[len(nums2) - N]:
                result.append(nums1[len(nums1) - M])
                M -= 1
            else:
                result.append(nums2[len(nums2) - N])
                N -= 1
            
        if M:
            for x in nums1[len(nums1) - M:]:
                result.append(x)
        
        if N:
            for x in nums2[len(nums2) - N:]:
                result.append(x)
        

        # return result
        
        if len(result) % 2 == 0:
            return (result[int(len(result) / 2 - 1)] + result[int(len(result) / 2)]) / 2
        else:
            return result[int((len(result)) // 2)]