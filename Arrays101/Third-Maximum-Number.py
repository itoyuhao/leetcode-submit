class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # sort 
        n = len(nums)
        
        if n < 3:
            return max(nums)
        
        for i in range(n-1):
            max_idx = i
            for j in range(i, n):
                if nums[max_idx] < nums[j]:
                    max_idx = j
            nums[max_idx], nums[i] = nums[i], nums[max_idx]
        
        rank = 1
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                rank += 1
            if rank == 3:
                return nums[i+1]
        
        return nums[0]